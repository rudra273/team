# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('refresh_captcha/', views.refresh_captcha, name='refresh_captcha'),
    path('success/', views.success, name='success'),
    
    
]
