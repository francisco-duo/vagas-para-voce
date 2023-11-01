from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vaga_para_voce.models.vagas_model import Vagas, Candidatar
from vaga_para_voce.forms import SearchForm
# from django.contrib.auth.decorators import login_required


def user_dashboard(request, ):
    if request.user.is_authenticated:
        usuario = {
            "nome": request.user.username,
            "email": request.user.email,
            'id': request.user.id
        }
        print(type(request.user.id))
        return render(request, 'site/pages/usuario.html', {'dados': usuario})
    else:
        return redirect('/login/')


def buscar_vagas(request, ):
    if request.user.is_authenticated:
        vagas = Vagas.objects.all()
        return render(request, 'site/pages/vagas.html', {'vagas': vagas})
    else:
        return redirect('/login/')


def criar_vagas(request, ):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'site/pages/cadastrar_vagas.html', )
        else:
            user = request.user
            titulo_vaga = request.POST.get('titulo_vaga')
            descricao = request.POST.get('descricao')

            cadastro = Vagas(
                dono_vaga=user,
                titulo_vaga=titulo_vaga,
                descricao_vaga=descricao
            )
            cadastro.save()

            return redirect('/usuario/')
    else:
        return redirect('/login/')


def search_vagas(request, ):
    if request.user.is_authenticated:
        if request.method == 'GET':

            query = request.GET.get('busca')
            vagas = Vagas.objects.filter(
                titulo_vaga__icontains=query
            )
            return render(request, 'search_results.html', {'vagas': vagas, 'query': query})
        return redirect('/usuario/')
    else:
        return redirect('/login/')
