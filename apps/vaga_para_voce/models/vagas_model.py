from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Vagas(models.Model):
    dono_vaga = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Empresa', blank=True)
    titulo_vaga = models.CharField(verbose_name='Título da vaga', max_length=255, blank=True)
    descricao_vaga = models.TextField(verbose_name='Descrição da vaga', blank=False)
    dt_criacao_vaga = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação', blank=True)


class Candidatar(models.Model):
    cadidato = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Cadidato', blank=True)
    vaga = models.ForeignKey(Vagas,on_delete=models.CASCADE, verbose_name='Vaga', blank=True)
    curriculo = models.FileField(upload_to='curriculos/')
    dt_canditato = models.DateTimeField(verbose_name='Data da candidatura', default=timezone.now)
