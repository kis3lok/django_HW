from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Review, Order
from .mistral import is_bad_review
from .telegram import send_telegram_message
from barbershop.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import asyncio

@receiver(post_save, sender=Review)
def check_review(sender, instance, created, **kwargs):
    if created:
        instance.ai_checked_status = "ai_checked_in_progress"
        instance.save()
        
        is_bad = is_bad_review(instance.text)
        
        if is_bad:
            instance.ai_checked_status = "ai_cancelled"
            instance.is_published = False
        else:
            instance.ai_checked_status = "ai_checked_true"
            instance.is_published = True
        instance.save()


@receiver(m2m_changed, sender=Order.services.through)
def telegram_order_notify(sender, instance, action, **kwargs):
    """
    Обработчик сигнала m2m_changed для модели Order.
    """

    if action == 'post_add' and kwargs.get('pk_set'):
        services = [service.name for service in instance.services.all()]
        message = (
            f"**Новый заказ {instance.date_created.strftime('%d.%m.%Y %H:%M')}**\n"
            f"Имя: {instance.client_name}\n"
            f"Телефон: {instance.phone}\n"
            f"Мастер: {instance.master.name}\n"
            f"Услуги: {', '.join(services) or 'Не указано'}\n"
            "---\n"
            f"Комментарий: {instance.comment or 'Не указан'}\n"
            f"#заказ #{instance.master.name}"
        )

        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message))