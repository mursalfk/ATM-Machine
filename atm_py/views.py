from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        return render(request, 'atm_py/welcome.html', {'title':'Welcome'})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        context = {'title':'Login'}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard-atm')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, 'atm_py/login2.html', context)
        
        return render(request, 'atm_py/login2.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login-atm')

def signuppage(request):
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Created for ' + user)
                return redirect('/')
        context = {'form' : form, 'title':'Signup'}
        # return render(request, 'atm_py/signup.html', {'title':'Signup'}, context)
        return render(request, 'atm_py/signup2.html', context)

# This line will restrict users to not to see the page if they are not signed in for every view we put above at
@login_required(login_url='/')
def dashboard(request):
    return render(request, 'atm_py/dashboard.html', {'title':'Dashboard'})
