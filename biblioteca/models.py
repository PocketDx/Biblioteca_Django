from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
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
    resumen = models.TextField()

    def __str__(self):
        # Mostrar título y autor en el admin
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
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Representación de la calificación
        return f"La Calificación de {self.libro.titulo} es {self.calificacion}/5"
    
    class Meta: # Definición de la clase Meta para personalizar el modelo
        # Se define el nombre de la tabla en la base de datos y los nombres en singular y plural
        db_table = 'biblioteca_resena'
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"