class Persona:
    def __init__(self, nombre, cedula,ti=None):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti
    def obtener_documento(self):
        return self.__cedula

    def get_cedula(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

persona1 = Persona("Ana", "123456789")  # Asumiendo sexo, ajusta si es necesario
persona2 = Persona("Luis", "987654321")  # Asumiendo sexo, ajusta si es necesario 
persona3 = Persona("Maria", "456789123")  # Asumiendo sexo, ajusta si es necesario  

print("el nombre de la primera persona es " , persona1.nombre )  # Acceso permitido

print("la cedula de la persona 1 es", persona1.obtener_documento()) # Acceso a través de método getter
print("la cedula de la persona 2 es", persona2.obtener_documento()) # Acceso a través de método getter
print("la cedula de la persona 3 es", persona3.obtener_documento()) #
