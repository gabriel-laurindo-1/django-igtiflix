from django.shortcuts import render
from serie.models import Serie


# Create your views here.

def index(request):
    serie_list = Serie.objects.all()
    data_dict = {'serie_list': serie_list}
    return render(request, 'principal/index.html', data_dict)