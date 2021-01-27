from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path('adminpanel/', admin.site.urls, name='top-atm'),
    path('', views.welcome, name="welcome-atm"),
    path('login/', views.loginpage, name="login-atm"),
    path('signup/', views.signuppage, name="signup-atm"),
    path('dashboard/', views.dashboard, name="dashboard-atm"),
    path('add_balance/', views.add_balance, name="add_balance_atm"),
    path('balance_inquiry/', views.balance_inquiry, name="balance_inquiry_atm"),
    path('change_password/', views.change_password, name="change_password_atm"),
    path('tranc_history/', views.tranc_history, name="tranc_history_atm"),
    path('withdraw_money/', views.withdraw_money, name="withdraw_money_atm"),
    path('logout/', views.logoutUser, name = 'logout-user'),
    # path('admin/')

]
