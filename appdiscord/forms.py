from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
   class Meta:
      model = Comentarios
      fields = ("nombre", "email", "website", "comentario")
      #fields = '__all__'
   # nombre = forms.CharField(widget=forms.TextInput(attrs('class': 'form-input')))