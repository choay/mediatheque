from django.shortcuts import render, get_object_or_404, redirect
from .models import Emprunteur, Livre, Cd, Dvd, JeuDePlateau
from .forms import EmprunteurForm, LivreForm, CdForm, DvdForm, JeuDePlateauForm


def menu_bibliothecaire(request):
    return render(request, 'bibliothecaire/menu_bibliothecaire.html')


def create_emprunteur(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_emprunteurs')
    else:
        form = EmprunteurForm()
    return render(request, 'bibliothecaire/create_emprunteur.html', {'form': form})


def list_emprunteurs(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/list_emprunteurs.html', {'emprunteurs': emprunteurs})


def update_emprunteur(request, pk):
    emprunteur = get_object_or_404(Emprunteur, pk=pk)
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=emprunteur)
        if form.is_valid():
            form.save()
            return redirect('list_emprunteurs')
    else:
        form = EmprunteurForm(instance=emprunteur)
    return render(request, 'bibliothecaire/update_emprunteur.html', {'form': form})


def list_medias(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'bibliothecaire/list_medias.html', {
        'livres': livres,
        'cds': cds,
        'dvds': dvds,
        'jeux': jeux,
    })


def create_emprunt(request, media_type, media_id):
    # Ajoutez votre logique pour créer un emprunt ici
    pass


def return_emprunt(request, media_type, media_id):
    # Ajoutez votre logique pour retourner un emprunt ici
    pass


def add_media(request, media_type):
    if media_type == 'livre':
        form_class = LivreForm
    elif media_type == 'cd':
        form_class = CdForm
    elif media_type == 'dvd':
        form_class = DvdForm
    elif media_type == 'jeu':
        form_class = JeuDePlateauForm
    else:
        return redirect('list_medias')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medias')
    else:
        form = form_class()

    return render(request, 'bibliothecaire/add_media.html', {'form': form})
