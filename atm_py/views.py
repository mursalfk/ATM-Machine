from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'atm_py/welcome.html', {'title':'Welcome'})

def login(request):
    return render(request, 'atm_py/login.html', {'title':'Login'})

def signup(request):
    return render(request, 'atm_py/signup.html', {'title':'Signup'})

def dashboard(request):
    return render(request, 'atm_py/dashboard.html', {'title':'Dashboard'})
