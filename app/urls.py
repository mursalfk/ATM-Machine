from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.splash_screen, name="splash-atm"),
    path('splash/', views.welcome, name="welcome-atm"),
    path('dashboard/', views.dashboard, name="dashboard-atm"),
    path('balance_inquiry/', views.balance_inquiry, name="balance_inquiry_atm"),
    path('withdraw_money/', views.withdraw_money, name="withdraw_money_atm"),
    path('tranc_history/', views.tranc_history, name="tranc_history_atm"),
    path('change_password/', views.change_password, name="change_password_atm"),
    path('add_balance/', views.add_balance, name="add_balance_atm"),
    # For Password Reset Email
    path('reset_password/', auth_views.PasswordResetView.as_view(), name = "reset_password"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "atm_py/password_reset_sent.html"),
    name='password_reset_done'),

    # Here uidb64 means the user id is encoded and the token is for validation 
    # of password
    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name = "atm_py/password_reset_form.html"),
    name = "password_reset_confirm"),
    
    
    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name = "atm_py/password_reset_done.html"),
    name='password_reset_complete'),

]
