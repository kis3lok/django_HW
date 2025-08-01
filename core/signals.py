from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from .mistral import is_bad_review

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