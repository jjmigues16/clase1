class Perro:
    def __init__(self, nombre, raza , edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"
#vamos instanciar un objeto ladrar
mi_perro = Perro("Moncho", "golden",7)
print(mi_perro.ladrar())
print(mi_perro.raza)
print( mi_perro.edad)
print("Clase Perro definida correctamente.")
mi_perro2 = Perro("choco", "pastor Aleman",1)

print(mi_perro2.ladrar())
print(mi_perro2.raza)
print(mi_perro2.edad)


nombre_perro = input("ingrese el nombre del perro: ")
raza_perro = input("ingrese la raza del perro:  ")
edad_perro = int(input("ingrese la edad del perro: "))
mi_perro3 = Perro(nombre_perro, raza_perro, edad_perro)
print(mi_perro3.ladrar())
class Persona:
    def __init__(self, nombre, edad,sexo, ):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años. Soy {self.sexo}."