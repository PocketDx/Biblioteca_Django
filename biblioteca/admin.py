from django.contrib import admin
from .models import Libro, Autor, Resena

# Register your models here

@admin.register(Autor)

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad'] # list_display define los campos que se mostrarán en la lista de objetos
    search_fields = ['nombre'] # search_fields define los campos que se utilizarán para buscar objetos en el admin
    list_filter = ['nacionalidad'] # list_filter define los campos que se utilizarán para filtrar objetos en el admin

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_publicacion', 'resumen']
    search_fields = ['titulo']
    list_filter = ['fecha_publicacion']

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['libro', 'texto', 'calificacion', 'fecha']
    search_fields = ['libro__titulo']
    list_filter = ['calificacion', 'fecha']