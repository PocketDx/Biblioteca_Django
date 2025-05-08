from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Validador personalizado para nombres vacíos o solo espacios
def validar_nombre_no_vacio(valor):
    if not valor.strip(): # Strip elimina los espacios en blanco al principio y al final de la cadena
        raise ValidationError('El nombre no puede estar vacío o solo contener espacios.')


# Validador para resumen mínimo
def validar_resumen_minimo(valor):
    if len(valor) < 50: # Len devuelve la longitud de la cadena
        raise ValidationError('El resumen debe tener al menos 50 caracteres.')


# Validador para calificación en rango
def validar_calificacion(valor):
    if valor < 0.0 or valor > 5.0: # Se valida que la calificación esté entre 0.0 y 5.0
        raise ValidationError('La calificación debe estar entre 0 y 5')

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre_no_vacio])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self): 
        # Se sobreescribe el método __str__ para mostrar el nombre del autor mas claro y legible
        return f"{self.nombre}"
    
    class Meta: # Definición de la clase Meta para personalizar el modelo
        # Se define el nombre de la tabla en la base de datos y los nombres en singular y plural
        db_table = 'biblioteca_autor'
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='libros'
    )
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen_minimo])

    def __str__(self):
        # Se sobreescribe el método __str__ para mostrar el título del libro y el nombre del autor de forma clara y legible
        return f"{self.titulo} ({self.autor.nombre})"
    
    class Meta: # Definición de la clase Meta para personalizar el modelo
        # Se define el nombre de la tabla en la base de datos y los nombres en singular y plural
        db_table = 'biblioteca_libro'
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Resena(models.Model):
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    texto = models.TextField()
    calificacion = models.FloatField(
        validators=[
            validar_calificacion, 
            MinValueValidator(0.0, message= "La calificación no puede ser menor a 0.0"), 
            MaxValueValidator(5.0, message= "La calificación no puede ser mayor a 5.0")
        ]
    )
    def __str__(self):
        # Se sobreescribe el método __str__ para mostrar la calificación del libro de forma clara y legible
        return f"La Calificación de {self.libro.titulo} es {self.calificacion}/5"
    fecha = models.DateTimeField(auto_now_add=True) 
        # Se establece la fecha y hora de creación de la reseña automáticamente
    
    class Meta: # Definición de la clase Meta para personalizar el modelo
        # Se define el nombre de la tabla en la base de datos y los nombres en singular y plural
        db_table = 'biblioteca_resena'
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"