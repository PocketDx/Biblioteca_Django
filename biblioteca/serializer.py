from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer): # Campo de serializador para el modelo Autor
    class Meta: # Definición de la clase Meta para personalizar el modelo
        model = Autor # Se define el modelo que se va a serializar
        fields = ['id', 'nombre', 'nacionalidad'] # Se definen los campos que se van a serializar

class LibroSerializer(serializers.ModelSerializer):
    recent_reviews = serializers.SerializerMethodField() # Campo personalizado para obtener reseñas recientes
    author = serializers.ReadOnlyField(source='autor.nombre')  # Read-only para mostrar el nombre del autor

    def get_recent_reviews(self, obj): # Método para obtener reseñas recientes
        reviews = obj.resenas.order_by('-fecha')[:5] # Se obtienen las 5 reseñas más recientes
        return ResenaSerializer(reviews, many=True).data
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'fecha_publicacion']  

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ['id', 'libro', 'calificacion']