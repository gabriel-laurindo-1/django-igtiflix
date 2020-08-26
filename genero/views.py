from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

# Create your views here.
def load_attrs_page(form, attr_name: str):
    generos_list = models.Genero.objects.order_by(attr_name)
    data_dict = {'form': form, 
                'generos_records': generos_list
                }
    return data_dict

def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR")
    data_dict = load_attrs_page(form=form, attr_name='descricao')
    return render(request, 'genero/genero.html', data_dict)

def delete(request, id):
    try:
        models.Genero.objects.filter(id=id).delete()
        form = forms.GeneroForm()
        data_dict = load_attrs_page(form=form, attr_name='descricao')
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()

def  update(request, id):
    item = models.Genero.objects.get(id=id)
    if request.method == "GET":
        form = forms.GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form': form}
        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        data_dict = load_attrs_page(form=form, attr_name='descricao')
        return render(request, 'genero/genero.html', data_dict)