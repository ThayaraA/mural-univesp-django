from django.shortcuts import render
from django.contrib import messages
from .models import Duvida


def index(request):
    context = {
        'duvida': Duvida.objects.all()
    }
    return render(request, 'index.html', context)

def professor(request):
    form = DuvidaForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']


            messages.success(request, 'Enviado com sucesso!')
            form = DuvidaForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail!')

    context = {
        'form':form
    }
    return render(request, 'professo.html', context)

def aluno(request):
    if str(request.method) == 'POST':
        form = DuvidaModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dúvida salva com sucesso!')
            form = DuvidaModelForm()
        else:
            messages.error(request, 'Erro ao salvar o Dúvida!')
    else:
        form = ProdutoModelForm()
    context = {
        'form':form
    }
    return render(request, 'aluno.html', context)
