from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'app/index.djt.html')


def register(request):
    return render(request, 'app/register.djt.html')
