from django import forms
from .models import Emprunteur, Livre, Cd, Dvd, JeuDePlateau

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'email', 'bloque']

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur', 'dateEmprunt', 'disponible', 'emprunteur']

class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'artiste', 'dateEmprunt', 'disponible', 'emprunteur']

class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ['name', 'realisateur', 'dateEmprunt', 'disponible', 'emprunteur']

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur', 'dateEmprunt', 'disponible', 'emprunteur']
