from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import ProdutoFinal
from django.contrib.auth.decorators import login_required
from .forms import ProdutoFinalForm


def ver_produto(request):
    produtos_finais = {
        'produtos_finais': ProdutoFinal.objects.all()
    }


    return render(request, 'producao/ver_produto.html', produtos_finais)


def inserir_produto(request):
    if request.method == 'POST':
        form = ProdutoFinalForm(request.POST)
        if form.is_valid():
            produto= form.save()
            request.session['produto'] = produto.pk 
            return redirect('inserir_produto')
    else:
        form = ProdutoFinalForm()
    return render(request, 'producao/inserir_produto.html', {'form':form} )

def editar_produto(request, id):
    produto = ProdutoFinal.objects.get(pk=id)
    form = ProdutoFinalForm(request.POST or None, instance = produto)
    if form.is_valid():
        form.save()
        return redirect('ver_produto')

    return render(request, 'producao/editar_produto.html', {'form':form} )

def deletar_produto(request, id):
    produto = ProdutoFinal.objects.get(pk=id)
    if request.method=="POST":
        produto.delete()
        return redirect('ver_produto')
    
    return render(request, 'producao/deletar_produto.html', {'produto':produto} )





# Create your views here.
