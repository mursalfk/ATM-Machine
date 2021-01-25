from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    context = {
        'title':'Welcome'
    }
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        return render(request, 'atm_py/welcome.html', context)

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

def accessAdmin(request):
    return redirect('admin-atm')

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

@login_required(login_url='/')
def add_balance(request):
    context = {
        'title':'Add Balance'
    }
    return render(request, 'atm_py/add_balance.html', context)
        
@login_required(login_url='/')
def balance_inquiry(request):
    context = {
        'title':'Balance Inquiry'
    }
    return render(request, 'atm_py/balance_inquiry.html', context)

@login_required(login_url='/')
def change_password(request):
    context = {
        'title':'Change Password'
    }
    return render(request, 'atm_py/change_password.html', context)

@login_required(login_url='/')
def tranc_history(request):
    context = {
        'title':'Transaction History'
    }
    return render(request, 'atm_py/tranc_history.html', context)

@login_required(login_url='/')
def withdraw_money(request):
    context = {
        'title':'Withdraw Money'
    }
    return render(request, 'atm_py/withdraw_money.html', context)