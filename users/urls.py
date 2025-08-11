from django.urls import path, reverse_lazy
from .views import (UserRegisterView, UserLoginView, UserLogoutView, UserProfileDetailView, UserProfileUpdateView,
                   CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, 
                   CustomPasswordResetCompleteView)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('profile/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='users/password_change_form.html',
             success_url=reverse_lazy('password_change_done')
         ), 
         name='password_change'),
    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'
         ), 
         name='password_change_done'),
    
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]