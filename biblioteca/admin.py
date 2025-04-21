from django.contrib import admin
from .models import Libro, Autor, Resena

# Register your models here

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_publicacion', 'resumen']
    search_fields = ['titulo']
    list_filter = ['fecha_publicacion']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad']
    search_fields = ['nombre']
    list_filter = ['nacionalidad']

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['libro', 'texto', 'calificacion', 'fecha']
    search_fields = ['libro__titulo']
    list_filter = ['calificacion', 'fecha']