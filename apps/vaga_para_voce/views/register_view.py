from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request, ):
    if request.method == "GET":
        return render(request, 'site/pages/cadastro.html')
    else:
        username = request.POST.get('name')
        email = request.POST.get('email')

        senha = request.POST.get('password')
        confirma_senha = request.POST.get('confirm_password')
        termo = request.POST.get('terms')

        if senha == confirma_senha and termo == 'terms':
            cadastro = User.objects.create_user(username, email, confirma_senha)
            cadastro.save()

            return redirect('/login/')
        else:
            return render(request, 'site/pages/cadastro.html')
