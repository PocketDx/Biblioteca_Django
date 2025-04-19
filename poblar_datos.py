from biblioteca.models import Autor, Libro, Resena

# Crear Autores
autor1 = Autor.objects.create(nombre='Gabriel García Márquez', nacionalidad='Colombiano')
autor2 = Autor.objects.create(nombre='Isabel Allende', nacionalidad='Chilena')
autor3 = Autor.objects.create(nombre='J.K. Rowling', nacionalidad='Británica')
autor4 = Autor.objects.create(nombre='George R.R. Martin', nacionalidad='Estadounidense')

# Crear Libros
libro1 = Libro.objects.create(
    titulo='Cien Años de Soledad',
    autor=autor1,
    fecha_publicacion='1967-01-01',
    resumen='Una novela emblemática de la literatura latinoamericana que narra la historia de la familia Buendía.',
)
libro2 = Libro.objects.create(
    titulo='La Casa de los Espíritus',
    autor=autor2,
    fecha_publicacion='1982-01-01',
    resumen='Obra maestra del realismo mágico que narra la saga de la familia Trueba.',
)
libro3 = Libro.objects.create(
    titulo='Harry Potter y la Piedra Filosofal',
    autor=autor3,
    fecha_publicacion='1997-06-26',
    resumen='El inicio de la famosa saga de Harry Potter, un joven mago que descubre su destino.',
)
libro4 = Libro.objects.create(
    titulo='Juego de Tronos',
    autor=autor4,
    fecha_publicacion='1996-08-06',
    resumen='El primer libro de la serie "Canción de Hielo y Fuego", una épica historia de intrigas y luchas por el trono.',
)

# Crear Reseñas
Resena.objects.create(libro=libro1, texto='Increíble narrativa, muy recomendable.', calificacion=5)
Resena.objects.create(libro=libro2, texto='Profunda y mágica, una lectura imprescindible.', calificacion=4)
Resena.objects.create(libro=libro3, texto='Una aventura mágica que atrapa desde el principio.', calificacion=5)
Resena.objects.create(libro=libro4, texto='Intriga y acción en cada página, excelente.', calificacion=4)
Resena.objects.create(libro=libro1, texto='Una obra maestra de la literatura.', calificacion=5)
Resena.objects.create(libro=libro2, texto='Una historia conmovedora y mágica.', calificacion=4)
Resena.objects.create(libro=libro3, texto='Un mundo fascinante lleno de magia.', calificacion=5)
Resena.objects.create(libro=libro4, texto='Una trama compleja y emocionante.', calificacion=4)