from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def adicionar(request):
    return render(request, 'adicionar.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')