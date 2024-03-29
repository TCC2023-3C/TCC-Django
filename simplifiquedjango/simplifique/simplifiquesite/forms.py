from django import forms
from .models import Comentario


class ComentarioForm(forms.Form):

    nome = forms.CharField(label="Nome", max_length=50, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    comentario = forms.CharField(
        label="Comentário", max_length=200, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
