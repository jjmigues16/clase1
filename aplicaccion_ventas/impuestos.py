from abc import ABC, abstractmethod
from typing import List
from modelos import Cliente, LineaFactura

class impuesto(ABC):
    @abstractmethod
    def calcular(self, cliente: Cliente, linea: LineaFactura) -> float:
        ...

class IVA(impuesto):
    def calcular(self, cliente: Cliente, linea: LineaFactura) -> float:
       return linea.subtotal * 0.19 if linea.producto.categoria != "alimentos" else 0.0
    
class Excecentos(impuesto):
    def calcular(self, cliente: Cliente, linea: LineaFactura) -> float:
       return linea.subtotal * 0.8 if linea.producto.categoria != "servicios" else 0.0
    
    