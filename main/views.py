from django.shortcuts import render
from .models import  Country


def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def bebrik(request):
    return render(request, 'main/bebrik.html')

def lolo(request):
    return render(request, 'main/lolo.html')

def blob(request):
    country = Country.objects.all()
    return render(request, 'main/blob.html', {'country': country} )