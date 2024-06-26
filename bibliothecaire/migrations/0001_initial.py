# Generated by Django 5.0.6 on 2024-06-11 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateEmprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('realisateur', models.CharField(max_length=100)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateEmprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('artiste', models.CharField(max_length=100)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateEmprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('createur', models.CharField(max_length=100)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateEmprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('auteur', models.CharField(max_length=100)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
