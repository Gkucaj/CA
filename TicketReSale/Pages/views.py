from django.shortcuts import render
from .models import event, Item

def index(request):
    return render(request, 'Pages/index.html')


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    (request, "item_list.html", context)
    return render