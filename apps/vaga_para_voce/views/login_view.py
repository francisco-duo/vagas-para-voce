from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django


def login(request, ):
    if request.method == "GET":
        return render(request, 'site/pages/login.html')
    else:
        email = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=email, password=senha)

        if user:
            login_django(request, user)
            return redirect('/usuario/')
        else:
            return redirect('/login/')


def logout(request, ):
    logout(request, )

    return redirect('/login/')