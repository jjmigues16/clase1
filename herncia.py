class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_snido(self):
        print(f"{self.nombre} hace un sonido")
    def jugar(self):
        print(f"{self.nombre} quiere jugar")

class Perro(Animal):
     def hacer_snido(self):
            print(f"{self.nombre} hace guau")

     def Salir_a_pasear(self):
        print(f"{self.nombre} está saliendo a pasear")
     
     def __init__(self,nombre,color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota
    
animal1 = Perro("Chocorramo", "azul")
animal1.hacer_snido()
animal1.Salir_a_pasear()
animal1.jugar()



class Gato(Animal):
     def hacer_snido(self):
            print(f"{self.nombre} hace miau")
     def Arenero(self):
            print(f"{self.nombre} está usando el arenero")
    
animal2 = Gato("Luna")
animal2.hacer_snido()
animal2.Arenero()
animal2.jugar()


print(isinstance(animal1, Perro))
print(isinstance(animal2, Gato))
print(isinstance(Perro, Gato))
print(isinstance(Gato, Animal))
