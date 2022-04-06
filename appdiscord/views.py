from django.shortcuts import render, redirect
from .models import Noticias, Descargas, Actualizacion, Comentarios
from .forms import ComentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView

# Create your views here.
def index (request):
    descarga = Descargas.objects.all()
    actualizacion = Actualizacion.objects.all()
    datos = {
        "Descargas" : descarga,
        "Actualizacion" : actualizacion
        
    }
    return render(request, 'app/index.html', datos)


def nosotros (request):
    return render(request, 'app/nosotros.html')

def basic (request):
    actualizaciones = Actualizacion.objects.all()
    comentario = Comentarios.objects.all()
    datos = {
        "Comentarios" : comentario,
        "Actualizacion": actualizaciones,
        "form": ComentariosForm
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/pages/basic-grid.html', datos)

def gallery (request):
    actualizaciones = Actualizacion.objects.all()
    datos = {
        "Actualizacion": actualizaciones
    }
    return render(request, 'app/pages/gallery.html', datos)

def full_width (request):
    actualizaciones = Actualizacion.objects.all()
    datos = {
        "Actualizacion": actualizaciones
    }
    return render(request, 'app/pages/full-width.html', datos)

def sidebarr (request):
    return render(request, 'app/pages/sidebar-right.html')
def sidebarl (request):
    noticia = Noticias.objects.all()
    actualizaciones = Actualizacion.objects.all()
    datos = {
        "Noticias" : noticia,
        "Actualizacion": actualizaciones
    }
    return render(request, 'app/pages/sidebar-left.html', datos)

def admin (request):
    return renser(request, '')


def notis (request):
    return render(request, 'app/pages/notis.html')


def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        descarga = Descargas.objects.filter(nombre_descarga__icontains=query)
        noticia = Noticias.objects.filter(encabezado__icontains=query)
        actualizacion = Actualizacion.objects.filter(nombre_act__icontains=query)
        datos = {
            "result" : descarga,
            "noticia": noticia,
            "actual" : actualizacion,
            "query" : query
        }
        return render(request, 'app/pages/busquedas.html', datos)
    else:
        return render(request, 'app/pages/busquedas.html')




class Registro(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'app/pages/registro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount created for {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super (Registro, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)