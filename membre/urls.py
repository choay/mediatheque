from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_membre, name='menu_membre'),
]
