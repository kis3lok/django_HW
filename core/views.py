from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from .models import Master, Service, Order, Review
from .forms import ReviewForm, OrderForm

class LandingView(TemplateView):
    template_name = 'landing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Главная страница',
            'masters': Master.objects.filter(is_active=True),
            'services': Service.objects.all(),
            'reviews': Review.objects.filter(is_published=True).select_related('master')[:6],
        })
        return context

class ThanksView(TemplateView):
    template_name = 'thanks.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Спасибо за заявку'
        return context

class OrdersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = 'orders_list.html'
    context_object_name = 'orders'
    ordering = ['-date_created']
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('master').prefetch_related('services')
        search_query = self.request.GET.get('search', '')
        
        if search_query:
            q_objects = Q()
            search_by_name = self.request.GET.get('search_by_name', 'on')
            search_by_phone = self.request.GET.get('search_by_phone', '')
            search_by_comment = self.request.GET.get('search_by_comment', '')
            
            if search_by_name:
                q_objects |= Q(client_name__icontains=search_query)
            if search_by_phone:
                q_objects |= Q(phone__icontains=search_query)
            if search_by_comment:
                q_objects |= Q(comment__icontains=search_query)
            
            if q_objects:
                queryset = queryset.filter(q_objects)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context.update({
            'title': 'Список заявок',
            'new_orders_count': queryset.filter(status='not_approved').count(),
            'confirmed_orders_count': queryset.filter(status='approved').count(),
            'completed_orders_count': queryset.filter(status='completed').count(),
            'cancelled_orders_count': queryset.filter(status='cancelled').count(),
            'search_query': self.request.GET.get('search', ''),
            'search_by_name': self.request.GET.get('search_by_name', 'on'),
            'search_by_phone': self.request.GET.get('search_by_phone', ''),
            'search_by_comment': self.request.GET.get('search_by_comment', ''),
        })
        return context

class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Заявка #{self.object.id}'
        return context

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = reverse_lazy('thanks')
    
    def form_valid(self, form):
        review = form.save(commit=False)
        review.is_published = False
        review.save()
        messages.success(self.request, 'Ваш отзыв успешно отправлен!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оставить отзыв'
        return context

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create_order.html'
    success_url = reverse_lazy('thanks')
    
    def form_valid(self, form):
        order = form.save(commit=False)
        order.status = 'not_approved'
        order.save()
        form.save_m2m()
        messages.success(self.request, 'Ваша заявка успешно отправлена!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записаться на услуги'
        return context