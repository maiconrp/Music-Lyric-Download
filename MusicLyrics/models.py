from django.db import models
from multiselectfield import MultiSelectField

class Pesquisa(models.Model):
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
        null = True,
        blank = True
    )
    nolyrics = models.BooleanField(
        default=False,
        null = True,
        blank = True)
    
    extra = MultiSelectField(
        max_length = 20,
        max_choices = 4,
        choices = EXTRA_CHOICES,
        null = True,
        blank = True
    )
    apikey = models.CharField(
        max_length=100,
        default='9ce9c5e4a931844f8c5f20cb9518e99b'
    )
    # result = models.JSONField(
    #     max_length=100,
    #     default = {'a':'a'},
    #     null = True,
    #     blank = True    
    # )
    
class Video(models.Model):
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

class Musica(models.Model):
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
    letra = models.TextField(
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
        related_name='Musica'
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='Musica'
    )


