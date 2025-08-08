import random

class Cuenta:
    def __init__(self, titular, saldo, numero_de_cuenta=None):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
            return self.saldo
        else:
            print("La cantidad a depositar debe ser positiva.")
            return -1
            
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
                return self.saldo
            else:
                print("Fondos insuficientes para realizar el retiro.")
                return -1
        else:
            print("La cantidad a retirar debe ser positiva.")
            return -1
            
    def consultar(self):
        return self.saldo

#programa principal
print("Bienvenido al sistema bancario")
cuentas = []
while True:
    print("\nSeleccione una opción:")
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Consultar saldo")
    print("5. Admin - ver número de cuenta y saldo")
    print("0. Salir")

    opcion = input("Opción: ")
    if opcion == "1":
        titular = input("Ingrese el nombre del titular: ")
        numero_de_cuenta = str(random.randint(100000, 999999))
        cuenta = Cuenta(titular, numero_de_cuenta, 0)
        cuentas.append(cuenta)
        print(f"Cuenta creada exitosamente. Su número de cuenta es: {numero_de_cuenta}")
    elif opcion == "2":
        numero_de_cuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        for cuenta in cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                nuevo_saldo = cuenta.depositar(cantidad)
                break
        else:
            print("Cuenta no encontrada.")
    elif opcion == "3":
        numero_de_cuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        for cuenta in cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                nuevo_saldo = cuenta.retirar(cantidad)
                break
        else:
            print("Cuenta no encontrada.")   
    elif opcion == "4":
        numero_de_cuenta = input("Ingrese el número de cuenta: ")
        for cuenta in cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                saldo = cuenta.consultar()
                print(f"El saldo de la cuenta {numero_de_cuenta} es: {saldo}")
                break
        else:
            print("Cuenta no encontrada.")
    elif opcion == "5":
        clave_admin = input("Ingrese la clave de administrador: ")
        if clave_admin != "admin123":
            print("Clave incorrecta. Acceso denegado.")
            continue
        print("Cuentas registradas:")
        for cuenta in cuentas:
            print(f"Número de cuenta: {cuenta.numero_de_cuenta}, Titular: {cuenta.titular}, Saldo: {cuenta.saldo}")
    elif opcion == "0":
        print("Hasta luego")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
