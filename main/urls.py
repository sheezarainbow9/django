from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),  # O campo vazio aqui leva à lista de alunos.
    path('aluno/<int:id>', views.alunoidView, name='aluno-view'),
    path('exemplo/', views.exemplo, name='exemplo'),
    path('newaluno/', views.newAluno, name='new-aluno'),
]
