from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField

class PesquisaVagalume(models.Model):
    EXTRA_CHOICES = (
        ("alb",     "Album"),
        ("relart",  "Artistas Relacionados"),
        ("relmus",  "Músicas Relacionadas"),
        ("rank",    "Ranking"),    
    )
    art = models.CharField(
        max_length=100,
        default=''
    ) 
    mus = models.CharField(
        max_length=100,
        default=''
    )
    musid = models.CharField(
        max_length=100,
        default=''
    )
    nolyrics = models.BooleanField(default=False)
    
    extra = MultiSelectField(
        max_length = 20,
        max_choices = 4,
        choices = EXTRA_CHOICES,
        null = True,
    )
    apikey = models.CharField(
        max_length=100,
        default='9ce9c5e4a931844f8c5f20cb9518e99b'
    )

class Artista(models.Model):
    id = models.CharField(
        max_length=17,
        default='',
        primary_key=True
    ) 
    name = models.CharField(
        max_length=100,
        default=''
    ) 
    url = models.URLField(
        max_length=100,
        default=''
    ) 

class Letra(models.Model):
    id = models.CharField(
        max_length=17,
        default='',
        primary_key=True
    ) 
    name = models.CharField(
        max_length=100,
        default=''
    ) 
    lang = models.CharField(
        max_length=100,
        default=''
    ) 
    url = models.URLField(
        max_length=100,
        default=''
    ) 
    text = models.TextField(
        max_length=2000,
        default=''
    ) 
    translate = models.TextField(
        max_length=2000,
        default='',
        null = True,
        blank = True
    ) 
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='Letra'
    )

class Musica(models.Model):
    id = models.CharField(
        max_length=11,
        default='',
        primary_key=True
    ) 
    title = models.CharField(
        max_length=100,
        default=''
    )
    description = models.TextField(
        max_length=1000,
        default=''
    )
    thumbnail = models.SlugField(
        max_length=100,
        default=''
    ) 
    duration = models.DurationField()

    letra = models.ForeignKey(
        Letra,
        on_delete=models.CASCADE,
        related_name='Musica'
    )
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='Musica'
    )

