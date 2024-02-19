from django.urls import path
from .views import *
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetConfirmView,
                                    PasswordResetCompleteView, 
                                       PasswordResetDoneView, PasswordResetView)  
app_name='users'

urlpatterns = [
    path('', register, name= 'register'), 

    path('login/', LoginView.as_view(template_name = 'users/login.html'), name= 'login'),

    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name= 'logout'), 
    
      path('accounts/profile/', user_profile, name= 'profile'),
    
    path('success/', success, name= 'success'), 
]

urlpatterns += [

    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ), name='password_reset_complete'), 

] 
