from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('news', views.news),
    path('bebrik', views.bebrik),
    path('lolo', views.lolo),
    path('blob', views.blob),
]

