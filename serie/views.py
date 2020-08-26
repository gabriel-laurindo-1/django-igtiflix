from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import models
from . import forms

# Create your views here.


def load_attrs_page(form, attr_name: str):
    series_list = models.Serie.objects.order_by(attr_name)
    data_dict = {'form': form,
                 'serie_records': series_list}
    return data_dict


def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("ERROR: Não foi possível cadastrar essa série.")
    data_dict = load_attrs_page(form=form, attr_name='nome')
    return render(request, 'serie/serie.html', data_dict)

def delete(request, id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieForm()
        data_dict = load_attrs_page(form=form, attr_name='nome')
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed()


def update(request, id):
    item = models.Serie.objects.get(id=id)
    if request.method == "GET":
        form = forms.SerieForm(initial={'nome': item.nome})
        data_dict = {'form': form}
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.nome = form.data['nome']
        item.save()
        data_dict = load_attrs_page(form=form, attr_name='nome')
        return render(request, 'serie/serie.html', data_dict)