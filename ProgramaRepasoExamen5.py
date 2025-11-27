# def aclarar_matriz    ->  Aclara un valor concreto a una imagen.

# Solo hace falta recorrer la matriz con esos dos bucles for (Uno para la fila, las listas, y el otro para las columnas, los elementos de la lista).
# Y sumando se aclara la imagen, es decir aumentar sus píxeles y hacerla más blanca.

# def invertir_matriz   ->  Invierte los valores de una imagen.

# Recorremos la matriz e invertimos los valores de la matriz restando el máximo (255) al resultado que tenemos para invertir el valor.

# def poner_diagonal_0  ->  Pone a 0 los valores de la diagonal, concretamente la superior.

# Recorremos la matriz y luego como queremos la matriz diagonal superior, solo entramos cuando la columna es mayor a la final y lo igualamos a 0.


def aclarar_matriz (matriz , valor ) :
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila) :
        for j in range (columna):
            matriz[i][j] += valor
    return matriz

def invertir_matriz (matriz):
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila):
        for j in range (columna):
            matriz[i][j] = 255 - matriz[i][j]
    return matriz
def poner_diagonal_0 (matriz):
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila):
        for j in range (columna):
            if j > i:
                matriz[i][j] = 0
    return matriz