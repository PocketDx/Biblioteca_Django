from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from biblioteca.views import AutorViewSet, LibroViewSet, ResenaViewSet

# Crear el router y registrar los ViewSets
router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'resenas', ResenaViewSet, basename='resena')

# Incluir las rutas del router bajo /api/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Se incluye la URL del router
]