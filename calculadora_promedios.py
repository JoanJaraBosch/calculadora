def ingresar_calificaciones():
    """
        Solicita al usuario ingresar materias y sus respectivas calificaciones.
        Permite sobrescribir materias repetidas y valida entrada numérica entre 0.00 y 10.00.
        Returns:
        tuple: Dos listas:
            - materias (list of str): nombres de las materias ingresadas.
            - calificaciones (list of float): calificaciones correspondientes a cada materia.
    """
    materias = []
    calificaciones = []

    while True:
        nombre = ""
        while nombre.strip() == "":
            nombre = input("Introduce el nombre de la materia que quieras añadir: ").strip().upper()

        if nombre in materias:
            respuesta = input("Ya has introducido esta materia, ¿quieres sobreescribir la nota? [S/N] ").strip().upper()
            if respuesta == "S":
                posicion = materias.index(nombre)
            else:
                continue
        else:
            materias.append(nombre)
            posicion = len(materias) - 1
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

    return materias, calificaciones                   

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Args:
        calificaciones (list of float): lista de calificaciones numéricas.
    Returns:
        float: promedio redondeado a dos decimales.
    """
    total = 0
    for nota in calificaciones:
        total = total + nota
    return round(total/len(calificaciones),2)

def determinar_estado(calificaciones, umbral = 5.00):
    """
    Clasifica las calificaciones en aprobadas y reprobadas según un umbral.
    Args:
        calificaciones (list of float): lista de calificaciones.
        umbral (float, optional): valor mínimo para aprobar. Por defecto es 5.00.
    Returns:
        tuple:
            - aprobadas (list of int): índices de materias aprobadas.
            - reprobadas (list of int): índices de materias reprobadas.
    """
    aprobadas = []
    reprobadas = []

    for i in range(0, len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    """
    Encuentra el índice de la nota máxima y mínima.
    Args:
        calificaciones (list of float): lista de calificaciones.
    Returns:
        tuple:
            - indice_maximo (int): índice de la calificación más alta.
            - indice_minimo (int): índice de la calificación más baja.
    """
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
    """
    Imprime si cada materia fue aprobada o reprobada.
    Args:
        materias (list of str): nombres de las materias.
        aprobadas (list of int): índices de materias aprobadas.
    """
    for i in range(0, len(materias)):
        if i in aprobadas:
            print(f"Materia {materias[i]} aprobada")
        else:
            print(f"Materia {materias[i]} reprobada")

def print_calificaciones(materias, calificaciones):
    """
    Muestra las calificaciones junto a sus respectivas materias.
    Args:
        materias (list of str): nombres de las materias.
        calificaciones (list of float): calificaciones de cada materia.
    """
    for i in range(0, len(materias)):
        print(f"Materia: {materias[i]}  ->  Nota: {calificaciones[i]:.2f}")

if __name__ == "__main__":
    materias, calificaciones = ingresar_calificaciones()
    try:
        umbral = float(input("\nHay alguna nota mínima para aprobar? (Pon el valor del umbral. Si no se pone valor se considerará 5.0 como umbral): "))
        if 10.00 < umbral or umbral <= 0.00:
            print("El umbral debe estar entre 0.00 y 10.00. Como no has especificado un valor correcto, el umbral será de 5.0")
            aprobadas, reprobadas = determinar_estado(calificaciones)
        else: 
            aprobadas, reprobadas = determinar_estado(calificaciones, umbral)
    except ValueError:
        print("Entrada no válida. Debías introducir un número. Como no has especificado un valor correcto, el umbral será de 5.0")
        aprobadas, reprobadas = determinar_estado(calificaciones)
    print("\nLas materias y las notas son las siguientes: ")
    print_calificaciones(materias, calificaciones)
    promedio = calcular_promedio(calificaciones)
    print(f"\nEl promedio de tus calificaciones es: {promedio:.2f}")
    print("\nA continuación te mostraremos las materias que has aprobado y cuales no: ")
    print_aprobado_reprobado(materias, aprobadas)

    print("\nLa maxima y minima nota es: ")
    maxima, minima = encontrar_extremos(calificaciones)
    print(f"La maxima nota es: {calificaciones[maxima]:.2f} en {materias[maxima]}")
    print(f"La minima nota es: {calificaciones[minima]:.2f} en {materias[minima]}")