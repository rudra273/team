from django import forms
from captcha.fields import CaptchaField
from  .models import visit
class LoginForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model=visit
        fields='__all__'
        
        
