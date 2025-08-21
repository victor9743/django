from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm

from .models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }

    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao Salvar contato')


    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):

    if str(request.user) != "AnonymousUser":
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
            else:
                messages.error(request, 'Erro ao salvar produto')
        form = ProdutoModelForm()
        
        context = {
            "form": form
        }

        return render(request, 'produto.html', context)
    else: 
        return redirect("index")