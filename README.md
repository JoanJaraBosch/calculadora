# Calculadora de Promedios Escolares en Python

## Descripción

Este programa en Python permite calcular el promedio de calificaciones escolares ingresadas por el usuario, utilizando programación estructurada y funciones básicas. El usuario puede ingresar múltiples materias y sus calificaciones (entre 0 y 10), y el programa muestra un resumen con el promedio general, materias aprobadas y reprobadas, y las materias con calificaciones máximas y mínimas.

## Funcionalidades

- Ingresar nombres de materias y sus calificaciones con validación.
- Calcular el promedio general de las calificaciones.
- Determinar materias aprobadas y reprobadas según un umbral (por defecto 5.0).
- Identificar la materia con la calificación más alta y la más baja.
- Permitir ingresar tantas materias como se desee.
- Mostrar un resumen final con toda la información procesada.

## Archivos

- `calculadora_promedios.py`: Contiene todo el código del programa.

## Instrucciones de uso

1. Ejecutar el programa con Python 3:
   ```bash
   python3 calculadora_promedios.py
   ```
2. Seguir las indicaciones para ingresar materias y calificaciones.
3. Consultar el resumen final con los resultados.

## Estructura del código

- `ingresar_calificaciones()`: Entrada y validación de materias y notas.
- `calcular_promedio(calificaciones)`: Cálculo del promedio.
- `determinar_estado(calificaciones, umbral=5.0)`: Clasificación en aprobados y reprobados.
- `encontrar_extremos(calificaciones)`: Encuentra calificaciones máxima y mínima.
- `main()`: Controla la ejecución general del programa.

## Requisitos

- Python 3.x

## Validaciones y manejo de errores

- Las calificaciones deben ser números entre 0 y 10.
- Permite ingresar múltiples materias y controlar la finalización de entrada.
- Maneja el caso en que no se ingrese ninguna materia.

## Licencia

Proyecto educativo, libre para uso y adaptación.
