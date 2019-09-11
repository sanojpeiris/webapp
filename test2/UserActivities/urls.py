from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("updateUser", views.updateUser, name="updateUser"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("home", views.moveToHome, name="home"),
    path("moveToLogin", views.moveToLogin, name="moveToLogin"),
    path("moveToRegister", views.moveToRegister, name="moveToRegister"),
    path("moveToUpdateUser", views.moveToUpdateUser, name="moveToUpdateUser"),
]
