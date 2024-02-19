from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    first_name = models.CharField(max_length=20, blank = True, null = True) 

    last_name = models.CharField(max_length=20, blank = True, null = True)

    contact_number = models.CharField(max_length=20, default = '9999999990',unique=True) 

    image = models.ImageField(upload_to= 'profile_images/' , default= 'profile.jpg')
    
    birthday = models.DateField(blank=True, null=True)
    
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
   
    location = models.CharField(max_length=50, blank=True)

    bio = models.TextField(max_length = 500, blank = True, null = True) 
    
    age=models.IntegerField(null=True, blank=True)
    def __str__(self) -> str:
        return self.user.username 




    
    