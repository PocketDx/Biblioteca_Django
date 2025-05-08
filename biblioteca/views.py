from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Autor, Libro, Resena
from .serializer import AutorSerializer, LibroSerializer, ResenaSerializer

# Create your views here.

class AutorViewSet(viewsets.ModelViewSet): # Vista para el modelo Autor
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer # Serializador para el modelo Autor

class LibroViewSet(viewsets.ModelViewSet): # Vista para el modelo Libro
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer # Serializador para el modelo Libro

    def get_queryset(self):
        if self.request.query_params.get('recent_reviews'):
            return self.queryset.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()
    
    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        libro = self.get_object()
        average_rating = libro.resenas.aggregate(Avg('calificacion'))['calificacion__avg']
        return Response({'average_rating': 0})

class ResenaViewSet(viewsets.ModelViewSet): # Vista para el modelo Reseña
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer # Serializador para el modelo Reseña