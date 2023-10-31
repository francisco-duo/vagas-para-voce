from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vaga_para_voce.models.vagas_model import Vagas, Candidatar
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


def visualizar_vaga(request, id):
    if request.user.is_authenticated:
        vaga = Vagas.objects.get(pk=id)
        return render(request, 'site/pages/vaga.html', {'vaga': vaga})
    else:
        return redirect('/login/')