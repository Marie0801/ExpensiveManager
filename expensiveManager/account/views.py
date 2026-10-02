import email

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("account")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from forms import LoginForm


def login_view(request):

    # form = LoginForm()

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")


        user = authenticate(
                request,
                email=email,
                password=password
            )

        if user:
                login(request, user)
                return redirect("login")

    return render(
        request,
        "account/login.html",
        
    )


def logout_view(request):
    logout(request)
    return redirect("login")