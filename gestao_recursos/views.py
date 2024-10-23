from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"gestao_recursos/index.html")
