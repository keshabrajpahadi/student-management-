from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,LoginForm
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
   return render(request,'studentauth/home.html')

def signup_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form =SignupForm()

        context = {
            'form': form
        }
        return render(request, 'studentauth/signup.html', context)
    return redirect('home')
def logout_user(request):
    logout(request)
    return redirect('home')
'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home')
            return HttpResponse("account not active")
        return HttpResponse("invalid login ")
    return render(request,'studentauth/login.html')
'''

@csrf_exempt
def login_user(request):
     if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                messages.success(request,'congratulations!! you have logged in ')
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()  # create form for GET request

        context = {'form': form}
        return render(request, 'studentauth/login.html', context)
     return redirect('home')