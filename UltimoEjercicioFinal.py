# EJERCICIO: GESTIÓN DE UN MINI-SISTEMA DE ESTUDIANTES
#
# Crea un programa que permita gestionar las notas de varios estudiantes de un curso.
#
# El programa debe:
# 1. Permitir introducir los nombres de los estudiantes y sus calificaciones de varias asignaturas.
#    - Cada estudiante tendrá un nombre (cadena) y una lista de notas (lista de enteros de 0 a 10).
#    - El usuario debe poder añadir tantos estudiantes como quiera, hasta introducir una cadena vacía.
#
# 2. Calcular automáticamente:
#    a) La media de cada estudiante y mostrar si aprueba o suspende (aprobado >= 5).
#    b) La nota máxima y mínima de cada estudiante.
#
# 3. Permitir buscar un estudiante por nombre y mostrar todas sus notas y su media.
#
# 4. Mostrar un ranking de los estudiantes ordenados por media de mayor a menor.
#
# 5. Calcular la media de la clase en cada asignatura.
#
# BONUS (opcional):
# 6. Detectar si algún estudiante tiene todas las notas iguales (por ejemplo: todas 8).
# 7. Mostrar cuántos estudiantes aprobaron todas las asignaturas.
#
# NOTAS:
# - Usa listas de listas o diccionarios para guardar los estudiantes y sus notas.
# - Debes practicar bucles, condicionales, listas, cadenas y funciones.
# - Comenta bien cada función para luego repasar antes del examen.


def obtener_datos():
    lista_datos = []
    nombre = input ("Introduce el nombre completo del estudiante :  \n")
    while nombre == "":
        nombre = input ("Nombre no válido, introduce un número válido : \n")
    lista_datos.append(nombre)
    notas = float (input ("Introduce cada nota individualmente (Introduce un valor no válido para acabar (0-10):   \n"))
    while notas < 0 or notas > 10:
        notas = float(input ("Dato incorrecto. Introduce la nota del 0 al 10: \n"))
    while 10 >= notas >= 0 :
        lista_datos.append(notas)
        notas = float (input("Introduce cada nota individualmente (Introduce un valor no válido para acabar (0-10):   \n"))
        if notas < 0 or notas > 10:
            break
    return lista_datos

def mostrar_info(lista):
    print(f"Estudiante: {lista[0]}")
    print("Notas:")
    for nota in lista[1:]:  #Notas del índice 1 hasta el final
        print(nota, end="  ")

def media_alumno(lista_num):
    media_persona = 0
    for nota in range (len(lista_num)):
        if nota >= 1:
            media_persona += lista_num[nota]
    media_persona = media_persona / (len(lista_num) - 1)
    if media_persona >= 5:
        print (f"\nEl estudiante ha tenido suerte y con su media de {media_persona} ha aprobado. ")
    else :
        print (f"\nEl estudiante no ha tenido suerte y con su media de {media_persona} ha suspendido. ")
    return media_persona

def nota_maxima_minima(lista): # Índice 1 primer número.
    nota_min = lista[1]
    nota_max = lista[1]
    for notas in range (len(lista)):
        if notas >= 1:
            if lista[notas] > nota_max:
                nota_max = lista[notas]
            if lista[notas] < nota_min:
                nota_min = lista[notas]
    print (f"La nota máxima del estudiante ha sido {nota_max}. Felicidades! \n")
    print (f"La peor nota ha sido {nota_min}. Muchos animos y a mejorar \n ")


def encontrar_alumno(lista_datos):
    nombre = input("Introduce el nombre de un estudiante a buscar: ")
    for alumno in lista_datos:
        if alumno[0].lower() == nombre.lower():
            print (f"El estudiante encontrado tiene estas notas: ")
            mostrar_info(alumno)
            media_alumno(alumno)
            nota_maxima_minima(alumno)
            return True
    print ("Estudiante no encontrado")
    return False

estudiantes = []

while True :
    estudiantes.append(obtener_datos())
    continuacion = input ("Quieres continuar añadiendo estudiantes? (S/N) \n")
    if continuacion != "S" :
        break
for i in range (len(estudiantes)):
    mostrar_info(estudiantes[i])

# Ejemplo xd