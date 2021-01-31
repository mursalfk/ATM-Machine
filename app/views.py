from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Balance_inq, TransactionHistory
from .forms import WithdrawMoney
from django.http import HttpResponse
import time

# Create your views here.
def splash_screen(request):
    context = {
        'title':'Welcome - ATM'
    }
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        return render(request, 'atm_py/splash.html', context)
    
def welcome(request):
    context = {
        'title':'Welcome'
    }
    if request.user.is_authenticated:
        return redirect('dashboard-atm')
    else:
        return render(request, 'atm_py/welcome.html', context)

@login_required(login_url='/')
def dashboard(request):
    # print(request.first_name)
    context = {
        'title' : 'Dashboard',
        'message' : 'Please Select an Option'
    }
    return render(request, 'atm_py/dashboard.html', context)

@login_required(login_url='/')
def change_password(request):
    context = {
        'title':'Change Password'
    }
    return render(request, 'atm_py/password_reset.html', context)

@login_required(login_url='/')
def balance_inquiry(request):
    user = request.user 
    # See this code for Zero Balance Withdrawal Thing
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
    flag = 1
    form = WithdrawMoney(request.POST or None)
    user = request.user 
    status = "Enter Amount"
    if Balance_inq.objects.filter(user_id = user).exists() == False:
        status = "New Account"
    if request.method == "POST":
        if form.is_valid():
            print('Form Submitted')
            try:
                amount = form.cleaned_data.get('amount')
                amount = int(amount) 
            except ValueError:
                flag = 0
            print(amount)
            if flag == 1:
                if Balance_inq.objects.filter(user_id = user).exists():
                    current_balance = Balance_inq.objects.get(user_id = user )
                    if amount > int(current_balance.balance):
                        status = "Insufficient Balance"
                    else:
                        # if current_balance <= 0 or current_balance :
                        current_balance.balance = int(current_balance.balance) - amount
                        print(current_balance)
                        remaining_ammount = current_balance.balance
                        td = TransactionHistory(user_id = user, remaining_amount = remaining_ammount, withdrawl_amount = amount)
                        current_balance.save()
                        td.save()
                        status = "Transaction Successful"
                        context = {
                            'message' : status,
                            'title' : 'Dashboard'
                        }
                        print(status)
                        return render(request, 'atm_py/dashboard.html', context)
                else:
                    status = "Insufficient/Zero Balance"
            else:
                status = "Please Enter a valid Amount"
    context = {
        'zero_balance_alert' : status,
        'form' : form,
        'title':'Withdraw Money'
    }
    return render(request, 'atm_py/withdraw_money.html', context)

@login_required(login_url='/')
def add_balance(request):
    flag = 1
    form = WithdrawMoney(request.POST or None)
    user = request.user 
    status = "Enter Amount"
    if Balance_inq.objects.filter(user_id = user).exists() == False:
        status = "New Account"
    if request.method == "POST":
        if form.is_valid():
            print('Form Submitted')
            try:
                amount = form.cleaned_data.get('amount')
                amount = int(amount) 
            except ValueError:
                flag = 0
            print(amount)
            if flag == 1:
                if Balance_inq.objects.filter(user_id = user).exists():
                    current_balance = Balance_inq.objects.get(user_id = user )
                    current_balance.balance = int(current_balance.balance) + amount
                    print(current_balance)
                    remaining_ammount = current_balance.balance
                    td = TransactionHistory(user_id = user, remaining_amount = remaining_ammount, withdrawl_amount = amount)
                    current_balance.save()
                    td.save()
                    status = "Balance Added Successful"
                    context = {
                        'message' : status,
                        'title' : 'Dashboard'
                    }
                    print(status)
                    return render(request, 'atm_py/dashboard.html', context)
                else:
                    inquiry = Balance_inq(user_id = user)
                    inquiry.balance = amount
                    inquiry.save()
                    
            else:
                status = "Please Enter a valid Amount"

    context = {
        'status' : status,
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

