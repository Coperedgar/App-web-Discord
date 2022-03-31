from django.contrib import admin
from .models import Noticias, Descargas, Actualizacion, Comentarios
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ["encabezado","descripcion","autor","fecha_creacion"]
    list_editable = ["autor"]
    search_fields = ["encabezado","descripcion","autor"]
    list_filter = ["fecha_creacion"]
    list_per_page = 10

class DescargaAdmin(admin.ModelAdmin):
    list_display = ["nombre_descarga", "enlace"]
    list_editable = ["enlace"]
    search_fields = ["nombre_descarga","enlace"]
    list_filter = ["nombre_descarga"]
    list_per_page = 10



class ActualizacionAdmin(admin.ModelAdmin):
    list_display = ["nombre_act","fecha_act"]
    list_editable = ["fecha_act"]
    search_fields = ["fecha_act"]
    list_per_page = 10

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","website","comentario"]
    list_editable = ["comentario"]
    search_fields = ["email"]
    list_per_page = 10 


admin.site.register(Noticias, NoticiaAdmin)
admin.site.register(Descargas, DescargaAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Actualizacion, ActualizacionAdmin)
