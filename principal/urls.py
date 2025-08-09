from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('acerca/', views.acerca, name='acerca'),
]