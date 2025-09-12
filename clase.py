class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def hacer_snido(self):
        print(f"{self.nombre} hace un sonido")

class Estudiante(Persona):
     def hacer_snido(self):
        print(f"{self.nombre} muchogusto de conocerte")
Estudiante1 = Estudiante("Ana")
Estudiante1.hacer_snido()            