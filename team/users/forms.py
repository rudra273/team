from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import User_Profile
from captcha.fields import CaptchaField
class NewRegisterForm(UserCreationForm): 

    email = forms.EmailField(required= True, widget= forms.EmailInput(attrs={'placeholder': 'demo@gmail.com', 'class': 'form-control'}))  

    username = forms.CharField(required=True, widget= forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))

    password1 = forms.CharField(label='Password',required=True, widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label= 'Re-enter password' ,required=True, widget= forms.PasswordInput(attrs={'class': 'form-control'}))   

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self,commit=True):
        user = super(NewRegisterForm,  self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save() 
        return user 

class ProfileForm(forms.ModelForm):
    captcha = CaptchaField(label='Enter the Captcha :',)
    class Meta:
        model=User_Profile
        fields='__all__'
        exclude=('user',)
        labels={'first_name':"FirstName :",
                'last_name':"LastName :",
                'contact_number':'Phone No.:',
                'age':"Age:",
                'birthday':'DOB:',
                'gender':"Gender:",
                'image':"Choose your pic :",
                'location':'Location:',
                'bio':'Bio:',
                }
        widgets = {
            # form-check
            'contact_number':forms.TextInput(attrs={'class': 'form-control mx-3',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mx-3',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mx-3',}),
            'birthday':forms.DateInput(attrs={'type':'date','class':'form-control mx-3'}),
            'age': forms.TextInput(attrs={'class': 'form-control mx-3',}),
            'image':forms.FileInput(attrs={'class':'form-control form-control-lg mx-3 '} ),
            'gender': forms.Select(attrs={'class': 'btn btn-info border border-2 dropdown-toggle mx-1 ',}),
            'location':forms.TextInput(attrs={'class':'form-control mx-4 mt-2'}),
            'bio':forms.Textarea(attrs={'class':'form-control mx-2 '}),
            }
             