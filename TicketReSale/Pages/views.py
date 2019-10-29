from django.shortcuts import render

from .models import event

def index(request):
    return render(request, 'Pages/index.html')
