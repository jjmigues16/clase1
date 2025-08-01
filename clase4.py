class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def average(self):
        return sum(self.grado) / len(self.grado)

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificaciones: {self.grado}")
        print(f"Promedio: {self.average():.2f}")

def main():
    estudiantes = []
    n = int(input("¿Cuántos estudiantes desea registrar? "))
    for i in range(n):
        print(f"\nRegistro del estudiante {i+1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        grados = []
        for j in range(3):
            while True:
                entrada = input(f"Calificación {j+1}: ")
                try:
                    calificacion = float(entrada)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido para la calificación.")
            grados.append(calificacion)
        estudiante = Estudiante(nombre, edad, grados)
        estudiantes.append(estudiante)

    print("\nDatos de los estudiantes:")
    for estudiante in estudiantes:
        estudiante.display()
        print("-" * 20)

if __name__ == "__main__":
    main()
print("estudiante registrado correctamente, gracias por su tiempo, hasta luego")