from django.shortcuts import render
from .data import *
from django.http import HttpResponse
# Create your views here.
def landing(request):
    context = {
        'masters': masters,
        'title': 'Barbershop "HR"'
    }
    return render(request, 'master_list.html', context)

def thanks(request):
    return render(request, 'thanks.html')

def order_list(request):
    context = {
        'orders': orders,
        'title': 'Заказы'
    }
    return render(request, 'orders.html', context)

def order_detailed(request, order_id):
    try:
        order_d = [order for order in orders if order['id'] == order_id][0]

    except IndexError:
        return HttpResponse("Заказ не найден", status=404)
    
    context = {
        "order": order_d,
    }
    return render(request, 'order_detailed.html', context)