from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.


def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos': alunos})


def alunoidView(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno': aluno})

def exemplo(request):
    if request.method == 'POST':
        name = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)

        print(name, email, telefone)
        #Aluno.objects.create(nome=name, email=email, telefone=telefone)

    return render(request, 'main/index.html')

def newAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect('/')
    else:
        form = AlunoForm()
    return render(request, 'main/add_aluno.html',  {'form':form})