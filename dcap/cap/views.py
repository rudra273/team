from django.shortcuts import render, redirect
from django.http import JsonResponse
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.conf import settings
from django.utils import timezone
from .forms import LoginForm
def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
     
            form.save()
            return redirect('success')
    else:
        form = LoginForm()
    
    # Generate captcha for the form
    new_captcha = CaptchaStore.generate_key()
    image_url = captcha_image_url(new_captcha)
    request.session['new_captcha_key'] = new_captcha

    context = {
        'form': form,
        'captcha_image_url': image_url,
        'captcha_timeout': settings.CAPTCHA_TIMEOUT,
    }
    return render(request, 'cap/login.html', context)

def success(request):
    return render(request, 'cap/success.html')

def refresh_captcha(request):
    new_captcha = CaptchaStore.generate_key()
    image_url = captcha_image_url(new_captcha)
    request.session['new_captcha_key'] = new_captcha
    return JsonResponse({'captcha_image_url': image_url})

