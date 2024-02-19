from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
    def save(self,  commit=True):
        user = super(SignUpForm,  self).save(commit=False)
        user.eamil = self.cleaned_data['email']
        if commit:
            user.save() 
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

   
