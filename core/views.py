from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Master, Service, Order, Review
from .forms import ReviewForm, OrderForm
from django.contrib import messages

def landing(request):
    """
    Главная страница с блоками мастеров и отзывов
    """
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('thanks'))
    
    masters = Master.objects.filter(is_active=True)
    reviews = Review.objects.filter(is_published=True).select_related('master')[:6]
    services = Service.objects.all()
    
    context = {
        'title': 'Главная страница',
        'masters': masters,
        'services': services,
        'reviews': reviews,
    }
    return render(request, 'landing.html', context)

def thanks(request):
    """
    Страница благодарности
    """
    context = {
        'title': 'Спасибо за заявку',
    }
    return render(request, 'thanks.html', context)

def create_review(request):
    """
    Создание отзыва
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_published = False
            review.save()
            messages.success(request, 'Ваш отзыв успешно отправлен!')
            return redirect('thanks')
    else:
        form = ReviewForm()
    
    context = {
        'title': 'Оставить отзыв',
        'form': form,
    }
    return render(request, 'create_review.html', context)

def create_order(request):
    """
    Создание заявки
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.status = 'not_approved'
            order.save()
            form.save_m2m()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('thanks')
    else:
        form = OrderForm()
    
    context = {
        'title': 'Записаться на услуги',
        'form': form,
    }
    return render(request, 'create_order.html', context)

def is_staff_user(user):
    """
    Проверка, является ли пользователь сотрудником
    """
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff_user)
def orders_list(request):
    """
    Список заявок с поиском по Q-объектам
    """
    orders = Order.objects.all().select_related('master').prefetch_related('services').order_by('-date_created')
    
    search_query = request.GET.get('search', '')
    search_by_name = request.GET.get('search_by_name', 'on')
    search_by_phone = request.GET.get('search_by_phone', '')
    search_by_comment = request.GET.get('search_by_comment', '')
    

    if search_query:
        q_objects = Q()
        
        if search_by_name:
            q_objects |= Q(client_name__icontains=search_query)
        
        if search_by_phone:
            q_objects |= Q(phone__icontains=search_query)
        
        if search_by_comment:
            q_objects |= Q(comment__icontains=search_query)
        
        if q_objects:
            orders = orders.filter(q_objects)
    
    new_orders_count = orders.filter(status='not_approved').count()
    confirmed_orders_count = orders.filter(status='approved').count()
    completed_orders_count = orders.filter(status='completed').count()
    cancelled_orders_count = orders.filter(status='cancelled').count()
    
    context = {
        'title': 'Список заявок',
        'orders': orders,
        'new_orders_count': new_orders_count,
        'confirmed_orders_count': confirmed_orders_count,
        'completed_orders_count': completed_orders_count,
        'cancelled_orders_count': cancelled_orders_count,
        'search_query': search_query,
        'search_by_name': search_by_name,
        'search_by_phone': search_by_phone,
        'search_by_comment': search_by_comment,
    }
    return render(request, 'orders_list.html', context)

@user_passes_test(is_staff_user)
def order_detail(request, order_id):
    """
    Детальная страница заявки
    """
    order = get_object_or_404(Order.objects.select_related('master').prefetch_related('services'), id=order_id)
    
    context = {
        'title': f'Заявка #{order_id}',
        'order': order,
    }
    return render(request, 'order_detail.html', context)