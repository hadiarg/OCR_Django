from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.about, name="about"),
    path('home/', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('loOutPage/', views.loOutPage, name="loOutPage"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
