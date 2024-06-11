from django.shortcuts import render
from bibliothecaire.models import Livre, Cd, Dvd, JeuDePlateau


def menu_membre(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'membre/menu_membre.html', {
        'livres': livres,
        'cds': cds,
        'dvds': dvds,
        'jeux': jeux,
    })
