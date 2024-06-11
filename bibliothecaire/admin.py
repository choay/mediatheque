from django.contrib import admin
from .models import Emprunteur, Livre, Cd, Dvd, JeuDePlateau

admin.site.register(Emprunteur)
admin.site.register(Livre)
admin.site.register(Cd)
admin.site.register(Dvd)
admin.site.register(JeuDePlateau)
