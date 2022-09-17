from django.db import models

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
    """
    type
art
    name
    url
mus
    id
    name
    lang
    url
    text
    translate
    """
# Create your models here.
