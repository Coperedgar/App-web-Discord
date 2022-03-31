from django.shortcuts import render
from .models import Noticias, Descargas, Actualizacion, Comentarios
from .forms import ComentariosForm

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

