from django.contrib import admin
from .models import User_Profile
# Register your models here.
from django.contrib.auth.models import User
admin.site.register(User_Profile)


