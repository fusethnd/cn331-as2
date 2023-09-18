from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("login", views.login, name="login"),
    path("main", views.main, name="main"),
]
