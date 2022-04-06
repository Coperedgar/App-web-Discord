"""discord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, nosotros, gallery, basic, sidebarr, sidebarl, full_width, buscar, admin, notis, Registro, CustomLoginView
from .forms import loginForm
from django.contrib.auth.models import views as auth_views

urlpatterns = [
    path('', index, name='inicio'),
    path('nosotros/',nosotros, name='nosotros'),
    path('galeria/',gallery, name='gallery'),
    path('comentarios/',basic, name='basic'),
    path('side/',sidebarr, name='side'),
    path('noticias/',sidebarl, name='sidebarl'),
    path('acerca_de/',full_width, name='full'),
    path('admin', admin, name='admin'),
    path('notis/', notis, name='notis'),
    path('buscar/', buscar, name='buscar'),
    path('registro/', Registro.as_view, name='registro'),
    path('login/', CustomLoginView.as_view(redirect authenticated_user=True, template_name='app/pages/login.html', authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/pages/logout.html'), name='logout'),    

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)