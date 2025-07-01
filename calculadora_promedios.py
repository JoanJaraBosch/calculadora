def ingresar_calificaciones():
    nombres = []
    calificaciones = []

    while True:
        nombre = ""
        while nombre.strip() == "":
            nombre = input("Introduce el nombre de la materia que quieras añadir: ").strip().upper()

        if nombre in nombres:
            respuesta = input("Ya has introducido esta materia, ¿quieres sobreescribir la nota? [S/N] ").strip().upper()
            if respuesta == "S":
                posicion = nombres.index(nombre)
            else:
                continue
        else:
            nombres.append(nombre)
            posicion = len(nombres) - 1
            calificaciones.append(0)  # valor temporal

        # Pedir y validar calificación
        while True:
            try:
                calificacion = float(input(f"Introduce la nota para {nombre} (0.00 - 10.00): "))
                if 0.00 <= calificacion <= 10.00:
                    calificaciones[posicion] = round(calificacion, 2)
                    break
                else:
                    print("La nota debe estar entre 0.00 y 10.00.")
            except ValueError:
                print("Entrada no válida. Debes introducir un número.")

        continuar = input("¿Quieres seguir introduciendo materias y notas? [S/N] ").strip().upper()
        if continuar != "S":
            break

    return nombres, calificaciones                   

def calcular_promedio(calificaciones):
    total = 0
    for nota in calificaciones:
        total = total + nota
    return round(total/len(calificaciones),2)

def determinar_estado(calificaciones, umbral = 5.00):
    aprobadas = []
    reprobadas = []

    for i in range(0, len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    maximo = -1
    indice_maximo = 0
    minimo = 11
    indice_minimo = 0

    for i in range(0, len(calificaciones)):
        if maximo < calificaciones[i]:
            maximo = calificaciones[i]
            indice_maximo = i

        if minimo > calificaciones[i]:
            minimo = calificaciones[i]
            indice_minimo = i
    return indice_maximo, indice_minimo

def print_aprobado_reprobado(materias, aprobadas):
    for i in range(0, len(materias)):
        if i in aprobadas:
            print(f"Materia {materias[i]} aprobada")
        else:
            print(f"Materia {materias[i]} reprobada")

def print_calificaciones(materias, calificaciones):
    for i in range(0, len(materias)):
        print(f"Materia: {materias[i]}  ->  Nota: {calificaciones[i]:.2f}")

if __name__ == "__main__":
     materias, calificaciones = ingresar_calificaciones()

     print("Las materias y las notas son las siguientes: ")
     print_calificaciones(materias, calificaciones)
     try:
        umbral = float(input("Hay alguna nota mínima para aprobar? (Pon el valor del umbral. Si no se pone valor se considerará 5.0 como umbral): "))
        if 10.00 < umbral or umbral <= 0.00:
            print("El umbral debe estar entre 0.00 y 10.00. Como no has especificado un valor correcto, el umbral será de 5.0")
            aprobadas, reprobadas = determinar_estado(calificaciones)
        else: 
            aprobadas, reprobadas = determinar_estado(calificaciones, umbral)
     except ValueError:
        print("Entrada no válida. Debíass introducir un número. Como no has especificado un valor correcto, el umbral será de 5.0")
        aprobadas, reprobadas = determinar_estado(calificaciones)

     print("A continuación te mostraremos las materias que has aprobado y cuales no.")
     print_aprobado_reprobado(materias, aprobadas)

     print("La maxima y minima nota es: ")
     maxima, minima = encontrar_extremos(calificaciones)
     print(f"La maxima nota es: {calificaciones[maxima]:.2f} en {materias[maxima]}")
     print(f"La minima nota es: {calificaciones[minima]:.2f} en {materias[minima]}")