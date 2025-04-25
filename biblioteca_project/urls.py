from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from biblioteca.views import AutorViewSet, LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'resenas', ResenaViewSet, basename='resena')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Se incluye la URL del router
]