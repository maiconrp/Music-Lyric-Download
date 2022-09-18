from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Pesquisa)
admin.site.register(Artista)
admin.site.register(Musica)
admin.site.register(Video)