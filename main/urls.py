from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('aluno/<int:id>', views.alunoidView, name='aluno-view'),
]