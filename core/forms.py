from django import forms
from .models import Review, Order, Master, Service


class ReviewForm(forms.ModelForm):
    """
    Форма создания отзыва
    """
    
    class Meta:
        model = Review
        fields = ['master', 'rating', 'client_name', 'text']
        widgets = {
            'master': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'required': True
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Поделитесь своими впечатлениями...',
                'required': True
            }),
        }
        labels = {
            'master': 'Выберите мастера',
            'rating': 'Оценка',
            'client_name': 'Ваше имя',
            'text': 'Отзыв',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master'].queryset = Master.objects.filter(is_active=True)
        self.fields['master'].empty_label = "Выберите мастера"


class OrderForm(forms.ModelForm):
    """
    Форма создания заявки
    """
    
    class Meta:
        model = Order
        fields = ['master', 'services', 'client_name', 'phone', 'comment', 'appointment_date']
        widgets = {
            'master': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'services': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67',
                'required': True
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительные пожелания...'
            }),
            'appointment_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'required': True
            }),
        }
        labels = {
            'master': 'Выберите мастера',
            'services': 'Выберите услуги',
            'client_name': 'Ваше имя',
            'phone': 'Телефон',
            'comment': 'Комментарий',
            'appointment_date': 'Дата и время записи',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master'].queryset = Master.objects.filter(is_active=True)
        self.fields['master'].empty_label = "Выберите мастера"
        self.fields['services'].queryset = Service.objects.all()

    def clean(self):
        """
        Валидация формы
        """
        cleaned_data = super().clean()
        master = cleaned_data.get('master')
        services = cleaned_data.get('services')

        if master and services:
            master_services = master.services.all()
            
            invalid_services = []
            for service in services:
                if service not in master_services:
                    invalid_services.append(service.name)
            
            if invalid_services:
                raise forms.ValidationError(
                    f"Мастер {master.name} не предоставляет следующие услуги: {', '.join(invalid_services)}"
                )

        return cleaned_data