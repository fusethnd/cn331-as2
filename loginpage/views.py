from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_page(request):
    return render(request, "login.html")

def main(request):
    return render(request, "main.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            return redirect("login_page")  # Redirect to the login page in case of failed authentication
    return render(request, "login.html")
