estudiantes = ['h','m','h','m','h','h','m']

cantidades = {'h': 0, 'm': 0}

for estudiante in estudiantes:
    if estudiante == 'h':
        cantidades['h'] += 1
    elif estudiante == 'm':
        cantidades['m'] += 1
    else:
        print("Género no reconocido:")

print(cantidades)
