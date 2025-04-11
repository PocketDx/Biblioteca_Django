from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        # Representación legible del autor
        return f"{self.nombre}"


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