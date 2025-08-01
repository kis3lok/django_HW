from django.contrib import admin
from .models import Master, Order, Review, Service

# Register your models here.
class MasterAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "is_active", "experience", "services_count"]
    search_fields = ["name", "phone"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    actions = ["make_active", "make_not_active"]

    @admin.display(description="Количество услуг")
    def services_count(self, obj):
        return obj.services.count()

    @admin.action(description="Активировать")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Деактивировать")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["client_name", "phone", "status", "services_count", "date_updated", "master"]
    search_fields = ["client_name", "phone"]
    list_filter = ["status"]
    list_editable = ["status"]
    actions = ["make_approved", "make_not_approved"]

    @admin.display(description="Количество услуг")
    def services_count(self, obj):
        return obj.services.count()

    @admin.action(description="Подтвердить")
    def make_approved(self, request, queryset):
        queryset.update(status="approved")

    @admin.action(description="Отменить")
    def make_not_approved(self, request, queryset):
        queryset.update(status="not_approved")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["client_name", "rating_digit", "created_at", "is_published"]
    search_fields = ["text", "client_name"]
    list_filter = ["created_at"]
    list_editable = ["is_published"]
    actions = ["make_published", "make_not_published"]

    @admin.display(description="Оценка")
    def rating_digit(self, obj):
        return obj.rating

    @admin.action(description="Опубликовать")
    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description="Снять с публикации")
    def make_not_published(self, request, queryset):
        queryset.update(is_published=False)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "duration", "masters_count", "is_popular"]
    search_fields = ["name", "description"]
    list_filter = ["price", "duration"]
    list_editable = ["price", "is_popular"]
    actions = ["make_popular", "make_not_popular"]

    @admin.display(description="Количество мастеров")
    def masters_count(self, obj):
        return obj.masters.count()

    @admin.action(description="Сделать популярным")
    def make_popular(self, request, queryset):
        queryset.update(is_popular=True)

    @admin.action(description="Сделать не популярным")
    def make_not_popular(self, request, queryset):
        queryset.update(is_popular=False)

admin.site.register(Master, MasterAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Service, ServiceAdmin)