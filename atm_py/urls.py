from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome-atm"),
    path('login/', views.loginpage, name="login-atm"),
    path('signup/', views.signuppage, name="signup-atm"),
    path('dashboard/', views.dashboard, name="dashboard-atm"),
    path('admin/', admin.site.urls, name='top-atm'),
    path('logout/', views.logoutUser, name = 'logout-user'),

]
