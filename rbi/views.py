from django.shortcuts import render, redirect
from rbi.models import Empresa
from rbi.forms import cadastroempresaForm, cadastroareaForm, cadastroequipForm, cadastrocomponenteForm, cadastropropostaForm


def index_view(request):
    empresas = Empresa.objects.all()
    context = {"rbi": empresas}
    return render(request, "index.html", context=context)

 
def cadastroempresa_view (request):
    if request.method == "POST":
      cadastroempresa_form = cadastroempresaForm(request.POST, request.FILES)
      if cadastroempresa_form.is_valid():
         cadastroempresa_form.save()
         return redirect("index")
         
    else:
      cadastroempresa_form = cadastroempresaForm()
    return render (request, 'cadastroempresa.html', {'cadastroempresa_form': cadastroempresa_form})


def cadastroarea_view (request):
    if request.method == "POST":
      cadastroarea_form = cadastroareaForm(request.POST, request.FILES)
      if cadastroarea_form.is_valid():
         cadastroarea_form.save()
         return redirect("index")
         
    else:
      cadastroarea_form = cadastroareaForm()
    return render (request, 'cadastroarea.html', {'cadastroarea_form': cadastroarea_form})

def cadastroequip_view (request):
    if request.method == "POST":
      cadastroequip_form = cadastroequipForm(request.POST, request.FILES)
      if cadastroequip_form.is_valid():
        cadastroequip_form.save()
        return redirect("index")
         
    else:
        cadastroequip_form = cadastroequipForm()
    return render (request, 'cadastroequip.html', {'cadastroequip_form': cadastroequip_form})

def cadastrocomponente_view (request):
    if request.method == "POST":
      cadastrocomponente_form = cadastrocomponenteForm(request.POST, request.FILES)
      if cadastrocomponente_form.is_valid():
        cadastrocomponente_form.save()
        return redirect("index")
         
    else:
        cadastrocomponente_form = cadastrocomponenteForm()
    return render (request, 'cadastrocomponente.html', {'cadastrocomponente_form': cadastrocomponente_form})



def cadastroproposta_view (request):
    if request.method == "POST":
      cadastroproposta_form = cadastropropostaForm(request.POST, request.FILES)
      if cadastroproposta_form.is_valid():
        cadastroproposta_form.save()
        return redirect("index")
         
    else:
        cadastroproposta_form = cadastropropostaForm()
    return render (request, 'cadastroproposta.html', {'cadastroproposta_form': cadastroproposta_form})
