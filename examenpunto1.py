class Libro:
    """Clase que representa un libro en la biblioteca"""
    
    def __init__(self, titulo, autor, año_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.año_publicacion}) - {self.genero}"


class Biblioteca:
    """Clase que administra una biblioteca personal de libros"""
    
    def __init__(self):
        # Decidí usar una lista para almacenar los libros porque:
        # 1. Las listas son mutables, permiten agregar y eliminar elementos dinámicamente
        # 2. Es más eficiente para búsquedas y operaciones de agregado
        # 3. Permite mantener el orden de inserción de los libros
        self.libros = []
    
    def registrar_libro(self, titulo, autor, año_publicacion, genero):
        """Registra un nuevo libro en la biblioteca"""
        nuevo_libro = Libro(titulo, autor, año_publicacion, genero)
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' registrado exitosamente.")
    
    def listar_libros(self):
        """Lista todos los libros registrados en la biblioteca"""
        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
            return
        
        print("\n--- LIBROS EN LA BIBLIOTECA ---")
        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro}")
        print("-------------------------------")
    
    def consultar_libro(self, titulo):
        """Consulta si un libro existe en la biblioteca por título"""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return True
        return False
    
    def obtener_total_libros(self):
        """Obtiene el total de libros guardados en la biblioteca"""
        return len(self.libros)


# Ejemplo de uso del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()
    
    # Registrar algunos libros de ejemplo
    biblioteca.registrar_libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico")
    biblioteca.registrar_libro("1984", "George Orwell", 1949, "Ciencia ficción")
    biblioteca.registrar_libro("El Quijote", "Miguel de Cervantes", 1605, "Novela")
    
    # Listar todos los libros
    biblioteca.listar_libros()
    
    # Consultar si un libro existe
    titulo_buscar = "1984"
    if biblioteca.consultar_libro(titulo_buscar):
        print(f"El libro '{titulo_buscar}' SÍ existe en la biblioteca.")
    else:
        print(f"El libro '{titulo_buscar}' NO existe en la biblioteca.")
    
    # Obtener el total de libros
    total = biblioteca.obtener_total_libros()
    print(f"\nTotal de libros en la biblioteca: {total}")
