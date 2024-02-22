from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewRegisterForm
from datetime import datetime,timedelta

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request,'session/index.html')

# creating session without user login
def session_withoutlogin(request):
    request.session['test']='testing'#creating session

    request.session['test']='moniska'#updating session

    request.session.pop('test',None) #deleting session  


    useTest='No user'
    if 'test' in request.session:
      useTest=request.session.get('test')
   
    context={'useTest':useTest}
    return render(request,'session/index.html',context)

# creating cookies
def cookie_(request):

    expire=datetime.now()+timedelta(days=1)
    response=render(request,"session/index.html")

    response.set_cookie(key='name3',value='monishka',expires=str(expire),secure=True)  # To create n update cookie
    # response.delete_cookie('name1') #To delete cookie

    # name=request.COOKIES.get('name')

    return response

# for testcookie  
@csrf_exempt
def testcookie(request):
    if request.method=='POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse('your browser can use cookie')
        return HttpResponse('Please enable cookies and try again')
    request.session.set_test_cookie()
    return render(request,'session/index.html')
    




def register(request): 

    if request.method == "POST":
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = NewRegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'session/register.html', context) 

