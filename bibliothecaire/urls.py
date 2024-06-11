from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_bibliothecaire, name='menu_bibliothecaire'),
    path('create_emprunteur/', views.create_emprunteur, name='create_emprunteur'),
    path('emprunteurs/', views.list_emprunteurs, name='liste_emprunteurs'),
    path('update_emprunteur/<int:pk>/', views.update_emprunteur, name='update_emprunteur'),
    path('medias/', views.list_medias, name='liste_medias'),
    path('create_emprunt/<str:media_type>/<int:media_id>/', views.create_emprunt, name='create_emprunt'),
    path('return_emprunt/<str:media_type>/<int:media_id>/', views.return_emprunt, name='return_emprunt'),
    path('add_media/<str:media_type>/', views.add_media, name='add_media'),
]
