from django.shortcuts import render


def home(request, ):
    return render(request, 'site/pages/home.html')


def login(request, ):
    return render(request, 'site/pages/login.html')