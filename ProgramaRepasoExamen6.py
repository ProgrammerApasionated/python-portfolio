# def obtener_notas ()                ->     Obtención de las notas de un usuario.

# def obtener_media (lista_notas)     ->     Obtención de la media de las notas.

# def racha_aprobados (lista_notas)   ->     Obtención de la racha de aprobados.

# def tipo_estudiante(lista_notas)    ->     Dependiendo de la media y la racha determinamos el tipo de estudiante.


def obtener_notas():
    notas = []
    cadena = 1
    while  0 <= cadena  <= 10 :
        cadena = float(input("Introduce una nota válida (Del 0 al 10):  \n"))
        if 0 > cadena or cadena > 10 :
            break
        else:
            print ("d")
            notas.append(cadena)
        print (notas)
    return notas

lista_notas = obtener_notas()
print (f"La lista de notas es {lista_notas}")