from django.urls import path
from . import views


urlpatterns = [
    path('', views.templates_view.home, name='home_page'),
    path('login/', views.login_view.login, name='login_page'),
    path('logout/', views.login_view.logout, name='logout'),
    path('cadastro/', views.register_view.register, name='register_page'),
    path('usuario/', views.users_view.user_dashboard, name='user_page'),
    path('cadastrar_vaga/', views.users_view.criar_vagas, name='cadastra_vaga'),
    path('vagas/', views.users_view.buscar_vagas, name='buscar_vaga'),
    # path('vaga/<id: int>', views.users_view.visualizar_vaga, name='visualizar_vaga'),
]
