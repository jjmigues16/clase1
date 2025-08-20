# ===== ¿QUÉ ES UN DICCIONARIO EN PYTHON? =====
# Un diccionario es una estructura de datos que almacena pares de datos
# en formato "clave: valor". Es como una agenda donde cada nombre (clave)
# tiene asociado un número de teléfono (valor).

# ===== PARA QUÉ SIRVE UN DICCIONARIO =====
# Sirve para organizar y acceder rápidamente a información relacionada.
# Es ideal cuando necesitas buscar valores usando identificadores únicos
# en lugar de posiciones numéricas como en las listas.

# Ejemplo práctico de diccionario
agenda = {
    "Juan": "555-1234",
    "María": "555-5678",
    "Carlos": "555-9012"
}

# Acceder a un valor usando su clave
telefono_juan = agenda["Juan"]  # Devuelve "555-1234"

# Agregar nuevo contacto
agenda["Ana"] = "555-3456"

# Modificar un contacto existente
agenda["Juan"] = "555-9999"

# Eliminar un contacto
del agenda["Carlos"]

print("Agenda actualizada:", agenda)

print("Teléfono de juan:", agenda["Juan"])  # Devuelve "555-5678"

estudiante = {
    "lucia": [4.5, 3.8, 4.2],
    "pedro": [3.5, 4.0, 3.9],
    "maria": [4.8, 4.6, 4.7]
}

# Acceder a las notas de un estudiante
print("Notas de Lucia:", estudiante)  
# coomo sacAR la nota promedio de todos los estudiantes
promedio = {}
for nombre, notas in estudiante.items():
    prom= sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {prom:.2f}")
    promedio[nombre] = prom #agregar al diccionario promedio

print("Promedio de notas:", promedio) #muestra el diccionario con los promedios

mejor_estudiante = max(promedio, key=promedio.get)  # Encuentra el estudiante con la nota más alta
print("El mejor estudiante es:", mejor_estudiante, "con un promedio de", promedio[mejor_estudiante])

peor_estudiante = min(promedio, key=promedio.get)  # Encuentra el estudiante con la nota más baja
print("El peor estudiante es:", peor_estudiante, "con un promedio de", promedio[peor_estudiante])