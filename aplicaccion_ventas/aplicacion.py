from modelos import Cliente, Producto
from pedido import factura
from descuento import SinDescuento, DescuentoVIP, DescuentoVolumen
from impuestos import IVA, Excecentos

cliente = Cliente(123,"Juan Perez", False)
producto1 = Producto(1, "Laptop", "electronica", 1500.0)
producto2 = Producto(2, "Manzanas", "alimentos", 3.0)
producto3 = Producto(3, "Servicio de limpieza", "servicios", 100.0)

mifactura = factura(cliente)
mifactura.agregar_linea(producto1, 1)
mifactura.agregar_linea(producto2, 5)   
mifactura.agregar_linea(producto3, 1)
descuento = DescuentoVIP()
impuesto = IVA()

print(f"Total de la factura: ${mifactura.calcular_total(descuento, impuesto):.2f}") 
