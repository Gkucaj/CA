from django.shortcuts import render
from .models import event, Item


def item_list(request):
    context = {
        'items': Item.objects.all
    }
    return render(request, "home-page.html", context)
