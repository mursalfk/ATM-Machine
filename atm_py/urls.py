from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome-atm"),
    path('login/', views.login, name="login-atm"),
    path('signup/', views.signup, name="signup-atm"),
    path('dashboard/', views.dashboard, name="dashboard-atm"),

    

]
