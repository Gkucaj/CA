from django.urls import path
from . import views
from .views import item_list

app_name='home'
app_name='event'
urlpatterns =[
    path('', views.index, name='index'),
    path("", item_list, name="item-list"),
]