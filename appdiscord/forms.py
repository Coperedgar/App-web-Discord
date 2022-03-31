from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
   class Meta:
      model = Comentarios
      fields = ("nombre", "email", "website", "comentario")
      #fields = '__all__' 
   nombre = forms.CharInput(widget=forms.TextInput(attrs=('class': 'form-input text-center input-black')))
   email = forms.EmailInput(widget=forms.TextInput(attrs=('class': 'form-input')))
   website = forms.URLInput(widget=forms.TextInput(attrs=('class': 'form-input')))
   comentario = forms.CharField(widget=forms.TextInput(attrs=('class': 'form-input')))