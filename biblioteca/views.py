from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Autor, Libro, Resena
from .serializer import AutorSerializer, LibroSerializer, ResenaSerializer

# Create your views here.

class AutorViewSet(viewsets.ModelViewSet): # Vista para el modelo Autor
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer # Serializador para el modelo Autor

    # Ejemplo de método personalizado
    def perform_create(self, serializer):
        nombre = serializer.validated_data.get('nombre')
        print(f"Creando autor: {nombre}")
        serializer.save()

class LibroViewSet(viewsets.ModelViewSet): # Vista para el modelo Libro
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer # Serializador para el modelo Libro
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['autor']  # Permite /api/books/?autor=1
    ordering_fields = ['titulo', 'id']  # Permite /api/books/?ordering=-titulo

    def get_queryset(self):
        queryset = Libro.objects.all()
        autor_id = self.request.query_params.get('author')
        if autor_id:
            queryset = queryset.filter(autor__id=autor_id)
        return queryset
    
    def get_queryset(self):
        if self.request.query_params.get('recent_reviews'): 
            return self.queryset.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()
    
    # Ruta personalizada: Promedio de calificación de un libro
    @action(detail=True, methods=['get'])
    def promedio_calificacion(self, request, pk=None):
        libro = self.get_object()
        avg_rating = libro.resenas.aggregate(Avg('calificacion'))['calificacion__avg']
        return Response({'Promedio de Calificación': avg_rating})

class ResenaViewSet(viewsets.ModelViewSet): # Vista para el modelo Reseña
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer # Serializador para el modelo Reseña