from django.shortcuts import render, get_object_or_404
from .models import Aluno

# Create your views here.
def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos': alunos})

def alunoidView(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno': aluno})