from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
   class Meta:
      model = Comentarios
      fields = ("nombre", "email", "website", "comentario")
      #fields = '__all__' 
   nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'required': 'true'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
   website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-input'}))
   comentario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))