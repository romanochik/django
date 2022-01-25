from django.shortcuts import render
# Creaet your views here
#from django.http import HttpRespsonse


def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def bebrik(request):
    return render(request, 'main/bebrik.html')