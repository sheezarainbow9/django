from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'aluno', AlunoViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),  # O campo vazio aqui leva à lista de alunos.
    path('aluno/<int:id>', views.alunoidView, name='aluno-view'),
    path('newaluno/', views.newAluno, name='new-aluno'),
    path('edit/<int:id>', views.editAluno, name='edit-aluno'),
    path('delete/<int:id>', views.deleteAluno, name='delete-aluno'),
]
