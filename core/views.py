from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .data import masters, services, orders, STATUS_NEW, STATUS_CONFIRMED, STATUS_CANCELLED, STATUS_COMPLETED

def landing(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('thanks'))
    
    context = {
        'title': 'Главная страница',
        'masters': masters,
        'services': services,
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

def is_staff_user(user):
    """
    Проверка, является ли пользователь сотрудником
    """
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff_user)
def orders_list(request):
    """
    Список заявок
    """
    new_orders_count = len([order for order in orders if order['status'] == STATUS_NEW])
    confirmed_orders_count = len([order for order in orders if order['status'] == STATUS_CONFIRMED])
    completed_orders_count = len([order for order in orders if order['status'] == STATUS_COMPLETED])
    cancelled_orders_count = len([order for order in orders if order['status'] == STATUS_CANCELLED])
    
    orders_with_masters = []
    for order in orders:
        order_copy = order.copy()
        master = next((m for m in masters if m['id'] == order['master_id']), None)
        order_copy['master'] = master['name'] if master else 'Не назначен'
        orders_with_masters.append(order_copy)
    
    context = {
        'title': 'Список заявок',
        'orders': orders_with_masters,
        'new_orders_count': new_orders_count,
        'confirmed_orders_count': confirmed_orders_count,
        'completed_orders_count': completed_orders_count,
        'cancelled_orders_count': cancelled_orders_count,
    }
    return render(request, 'orders_list.html', context)

@user_passes_test(is_staff_user)
def order_detail(request, order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    
    if not order:
        raise Http404("Заявка не найдена")
    
    order_copy = order.copy()
    master = next((m for m in masters if m['id'] == order['master_id']), None)
    order_copy['master'] = master['name'] if master else 'Не назначен'
    
    context = {
        'title': f'Заявка #{order_id}',
        'order': order_copy,
    }
    return render(request, 'order_detail.html', context)

def order_list(request):
    return orders_list(request)

def order_detailed(request, order_id):
    return order_detail(request, order_id)