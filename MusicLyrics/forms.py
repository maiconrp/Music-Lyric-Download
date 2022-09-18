from django import forms
from MusicLyrics.models import *

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = "__all__"

        