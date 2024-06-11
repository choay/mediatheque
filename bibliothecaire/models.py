from django.db import models
from django.utils import timezone


class Emprunteur(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Livre(Media):
    auteur = models.CharField(max_length=100)


class Cd(Media):
    artiste = models.CharField(max_length=100)


class Dvd(Media):
    realisateur = models.CharField(max_length=100)


class JeuDePlateau(Media):
    createur = models.CharField(max_length=100)
