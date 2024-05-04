from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from user.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "user/register.html", {"form": form})
    
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            return redirect("/login/")
        return render(request, "user/register.html", {"form": form})


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})
    
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            form.add_error(None, "Неверное имя пользователя или пароль")
        return render(request, "user/login.html", {"form": form})
    

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, "user/profile.html")