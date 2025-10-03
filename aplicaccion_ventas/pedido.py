from abc import ABC, abstractmethod
from typing import List
from modelos import Cliente, LineaFactura, Producto
from descuento import  SinDescuento, DescuentoVIP, DescuentoVolumen, Descuento
from impuestos import impuesto, IVA, Excecentos, impuesto
from dataclasses import dataclass, field

@dataclass
class factura:
    cliente: Cliente
    lineas: List[LineaFactura]= field (default_factory=list)

    def agregar_linea(self, producto: Producto, cantidad: int):
        self.lineas.append(LineaFactura(producto, cantidad))

    def calcular_descuento(self, descuento: Descuento):
        total_descuento = 0 
        for i in self.lineas:
         total_descuento = total_descuento + descuento.aplicar(self.cliente, i)

        return total_descuento
        ##return sum(descuento.aplicar(self.cliente, l) for l in self.lineas)###
    def calcular_impuesto(self, impuesto: impuesto):
        for i in self.lineas:
         total_impuesto = 0
         total_impuesto = total_impuesto + impuesto.calcular(self.cliente, i)

        return total_impuesto
        ##return sum(impuesto.calcular(self.cliente, l) for l in self.lineas)###

    def calcular_total(self, descuento: Descuento, impuesto: impuesto):
        subtotal = sum(l.total for l in self.lineas)
        total_descuento = self.calcular_descuento(descuento)
        total_impuesto = self.calcular_impuesto(impuesto)
        total = subtotal - total_descuento + total_impuesto
        return total