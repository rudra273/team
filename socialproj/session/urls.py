from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView  

app_name='session'

urlpatterns = [
    path('index/',index,name='index'),
    path('', register, name= 'register'), 

    path('session/', session_withoutlogin, name= 'session_withoutlogin'), 
    path('cookie/', cookie_, name='cookie'), 
    path('testcookie/', testcookie, name='testcookie'), 


    path('login/', LoginView.as_view(template_name = 'session/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'session/logout.html'), name= 'logout'), 
]


