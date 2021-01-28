from django.shortcuts import render, redirect
# from .forms import CreateUserForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Balance_inq, TransactionHistory
from .forms import WithdrawMoney


# Create your views here.

@login_required(login_url='/')
def dashboard(request):
    return render(request, 'atm_py/dashboard.html', {'title':'Dashboard'})

@login_required(login_url='/')
def change_password(request):
    context = {
        'title':'Change Password'
    }
    return render(request, 'atm_py/change_password.html', context)

@login_required(login_url='/')
def balance_inquiry(request):
    user = request.user 
    if Balance_inq.objects.filter(user_id = user).exists():
        current_balance = Balance_inq.objects.all().filter(user_id = user )
        for e in current_balance:
            print(e.balance)
            current_balance = e.balance
    else:
        current_balance = 'Zero'
    context = {
        'title':'Balance Inquiry',
        'current_balance' : current_balance,
    }
    return render(request, 'atm_py/balance_inquiry.html', context)

@login_required(login_url='/')
def withdraw_money(request):
    form = WithdrawMoney(request.POST or None)
    user = request.user 
    if request.method == "POST":
        if form.is_valid():
            print('Form Submitted')
            amount = form.cleaned_data.get('amount')
            amount = int(amount)
            print(amount)
            if Balance_inq.objects.filter(user_id = user).exists():
                current_balance = Balance_inq.objects.get(user_id = user )
                current_balance.balance = int(current_balance.balance) - amount
                print(current_balance)
                remaining_ammount = current_balance.balance
                td = TransactionHistory(user_id = user, remaining_amount = remaining_ammount, withdrawl_amount = amount)
                current_balance.save()
                td.save()
    context = {
        'form' : form,
        'title':'Withdraw Money'
    }
    return render(request, 'atm_py/withdraw_money.html', context)

@login_required(login_url='/')
def add_balance(request):
    form = WithdrawMoney(request.POST or None)
    user = request.user 
    if request.method == "POST":
        if form.is_valid():
            print('Form Submitted')
            amount = form.cleaned_data.get('amount')
            amount = int(amount)
            print(amount)
            if Balance_inq.objects.filter(user_id = user).exists():
                current_balance = Balance_inq.objects.get(user_id = user )
                current_balance.balance = int(current_balance.balance) + amount
                print(current_balance)
                remaining_ammount = current_balance.balance
                td = TransactionHistory(user_id = user, remaining_amount = remaining_ammount, withdrawl_amount = amount)
                current_balance.save()
                td.save()
    context = {
        'form' : form,
        'title':'Add Balance'
    }
    return render(request, 'atm_py/add_balance.html', context)



@login_required(login_url='/')
def tranc_history(request):
    user = request.user 
    td = TransactionHistory.objects.filter(user_id = user)
    context = {
        'history_td' : td,
        'title':'Transaction History',
    }
    return render(request, 'atm_py/tranc_history.html', context)