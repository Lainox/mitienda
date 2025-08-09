from django.shortcuts import render

def inicio(request):
    return render(request, 'principal/index.html')

def acerca(request):
    return render(request, 'principal/about.html')