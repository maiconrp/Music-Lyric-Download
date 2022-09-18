from django import forms
from MusicLyrics.models import *

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = "__all__"

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = "__all__"

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = "__all__"

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
