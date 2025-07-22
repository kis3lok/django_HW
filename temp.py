from django.contrib import admin
from django.urls import path
from core.views import landing, thanks, orders_list, order_detail, create_review, create_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('thanks/', thanks, name='thanks'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('review/create/', create_review, name='create_review'),
    path('order/create/', create_order, name='create_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






4. Создание шаблонов
Создадим шаблон для создания отзыва:

{% extends "base.html" %}
{% load static %}

{% block title %}Оставить отзыв - Барбершоп "Hard Rock"{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card shadow">
                <div class="card-header bg-primary text-white">
                    <h2 class="mb-0">
                        <i class="bi bi-chat-quote"></i> Оставить отзыв
                    </h2>
                </div>
                <div class="card-body">
                    <p class="text-muted mb-4">
                        Поделитесь своими впечатлениями о работе наших мастеров. 
                        Ваш отзыв поможет другим клиентам сделать правильный выбор.
                    </p>

                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}

                    <form method="post" novalidate>
                        {% csrf_token %}
                        
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="{{ form.master.id_for_label }}" class="form-label">
                                    {{ form.master.label }} <span class="text-danger">*</span>
                                </label>
                                {{ form.master }}
                                {% if form.master.errors %}
                                    <div class="text-danger small mt-1">
                                        {{ form.master.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            
                            <div class="col-md-6 mb-3">
                                <label for="{{ form.rating.id_for_label }}" class="form-label">
                                    {{ form.rating.label }} <span class="text-danger">*</span>
                                </label>
                                {{ form.rating }}
                                {% if form.rating.errors %}
                                    <div class="text-danger small mt-1">
                                        {{ form.rating.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="{{ form.client_name.id_for_label }}" class="form-label">
                                {{ form.client_name.label }} <span class="text-danger">*</span>
                            </label>
                            {{ form.client_name }}
                            {% if form.client_name.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.client_name.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="mb-4">
                            <label for="{{ form.text.id_for_label }}" class="form-label">
                                {{ form.text.label }} <span class="text-danger">*</span>
                          </label>
                            {{ form.text }}
                            {% if form.text.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.text.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <a href="{% url 'landing' %}" class="btn btn-secondary me-md-2">
                                <i class="bi bi-arrow-left"></i> Отмена
                            </a>
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-send"></i> Отправить отзыв
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}    




///


Создадим шаблон для создания заявки:

{% extends "base.html" %}
{% load static %}

{% block title %}Записаться на услуги - Барбершоп "Hard Rock"{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card shadow">
                <div class="card-header bg-primary text-white">
                    <h2 class="mb-0">
                        <i class="bi bi-calendar-check"></i> Записаться на услуги
                    </h2>
                </div>
                <div class="card-body">
                    <p class="text-muted mb-4">
                        Заполните форму ниже, чтобы записаться к одному из наших мастеров. 
                        Мы свяжемся с вами для подтверждения записи.
                    </p>

                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}

                    <form method="post" novalidate>
                        {% csrf_token %}
                        
                        <div class="mb-3">
                            <label for="{{ form.master.id_for_label }}" class="form-label">
                                {{ form.master.label }} <span class="text-danger">*</span>
                            </label>
                            {{ form.master }}
                            {% if form.master.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.master.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="mb-3">
                            <label class="form-label">
                                {{ form.services.label }} <span class="text-danger">*</span>
                            </label>
                            <div class="row">
                                {% for choice in form.services %}
                                    <div class="col-md-6 mb-2">
                                        <div class="form-check">
                                            {{ choice.tag }}
                                            <label class="form-check-label" for="{{ choice.id_for_label }}">
                                                {{ choice.choice_label }}
                                            </label>
                                        </div>
                                    </div>
                                {% endfor %}
                            </div>
                            {% if form.services.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.services.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="{{ form.client_name.id_for_label }}" class="form-label">
                                    {{ form.client_name.label }} <span class="text-danger">*</span>
                                </label>
                                {{ form.client_name }}
                                {% if form.client_name.errors %}
                                    <div class="text-danger small mt-1">
                                        {{ form.client_name.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            
                            <div class="col-md-6 mb-3">
                                <label for="{{ form.phone.id_for_label }}" class="form-label">
                                    {{ form.phone.label }} <span class="text-danger">*</span>
                                </label>
                                {{ form.phone }}
                                {% if form.phone.errors %}
                                    <div class="text-danger small mt-1">
                                        {{ form.phone.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="{{ form.appointment_date.id_for_label }}" class="form-label">
                                {{ form.appointment_date.label }} <span class="text-danger">*</span>
                            </label>
                            {{ form.appointment_date }}
                            {% if form.appointment_date.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.appointment_date.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="mb-4">
                            <label for="{{ form.comment.id_for_label }}" class="form-label">
                                {{ form.comment.label }}
                            </label>
                            {{ form.comment }}
                            {% if form.comment.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.comment.errors }}
                                </div>
                            {% endif %}
                        </div>

                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <a href="{% url 'landing' %}" class="btn btn-secondary me-md-2">
                                <i class="bi bi-arrow-left"></i> Отмена
                            </a>
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-calendar-check"></i> Записаться
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}


////


Обновление навигационного меню
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'landing' %}">
            <i class="bi bi-scissors"></i> Hard Rock
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'landing' %}#about">О нас</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'landing' %}#services">Услуги</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'landing' %}#masters">Мастера</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'create_order' %}">
                        <i class="bi bi-calendar-check"></i> Записаться
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'create_review' %}">
                        <i class="bi bi-chat-quote"></i> Отзыв
                    </a>
                </li>
                {% if user.is_staff %}
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'orders_list' %}">
                        <i class="bi bi-list-ul"></i> Заявки
                    </a>
                </li>
                {% endif %}
            </ul>
            
            <ul class="navbar-nav">
                {% if user.is_authenticated %}
                <li class="nav-item">
                    <span class="navbar-text">
                        <i class="bi bi-person-circle"></i> {{ user.username }}
                    </span>
                </li>
                {% else %}
                <li class="nav-item">
                    <a class="nav-link" href="#login">
                        <i class="bi bi-box-arrow-in-right"></i> Вход
                    </a>
                </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>


Обновление страницы благодарности
{% extends "base.html" %}
{% load static %}

{% block title %}Спасибо за заявку - Барбершоп "Hard Rock"{% endblock %}

{% block content %}
<div class="container" id="thanks-page" data-redirect-url="{% url 'landing' %}" data-countdown="10">
    <div class="row justify-content-center">
        <div class="col-lg-8 text-center py-5">
            <div class="card shadow-lg">
                <div class="card-body py-5">
                    <i class="bi bi-check-circle-fill text-success display-1 mb-4"></i>
                    <h1 class="card-title text-success mb-4">Спасибо за заявку!</h1>
                    <p class="card-text lead mb-4">
                        Ваша заявка успешно отправлена. Наш администратор свяжется с вами в ближайшее время для подтверждения записи.
                    </p>
                    <div class="mb-4">
                        <p class="text-muted">Автоматический переход на главную страницу через: <span id="countdown">10</span> секунд</p>
                    </div>
                    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                        <a href="{% url 'landing' %}" class="btn btn-primary btn-lg">
                            <i class="bi bi-house"></i> Вернуться на главную
                        </a>
                        <a href="{% url 'create_order' %}" class="btn btn-outline-primary btn-lg">
                            <i class="bi bi-plus-circle"></i> Оставить еще заявку
                        </a>
                        <a href="{% url 'create_review' %}" class="btn btn-outline-success btn-lg">
                            <i class="bi bi-chat-quote"></i> Оставить отзыв
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
console.log('Thanks page script loaded');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, starting countdown');
    
    let countdown = 10;
    const countdownElement = document.getElementById('countdown');
    
    if (!countdownElement) {
        console.error('Countdown element not found');
        return;
    }
    
    console.log('Countdown element found, starting timer');
    
    window.thanksTimer = setInterval(function() {
        countdown--;
        console.log('Countdown:', countdown);
        countdownElement.textContent = countdown;
        
        if (countdown <= 0) {
            console.log('Redirecting to landing page');
            clearInterval(window.thanksTimer);
            window.location.href = "{% url 'landing' %}";
        }
    }, 1000);
    
    window.addEventListener('beforeunload', function() {
        if (window.thanksTimer) {
            clearInterval(window.thanksTimer);
        }
    });
});
</script>
{% endblock %}