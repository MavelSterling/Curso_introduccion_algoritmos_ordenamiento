# 1. Buscar el numero menor en mi array
# 2. Crear dos subarrays para llevar el control del algoritmo
# 3. imprimir el resultado del ordenamiento

import sys

array=[20, 5, 21, 6, 23, 7, 34, 999, 68]

def selectionSort(array):
    # recorrer todo nuestro array
    for i in range(len(array)):

        # Encontrar el valor mínimo restante dentro de nuestro array desordenado
        idxDes = i # al iniciar i es 0

        for j in range(i+1,len(array)): 
            if array[idxDes] > array[j]:
                idxDes = j

        # ya que encontramos el minimo, se cambia por el primer valor del array desordenado
        array[i], array[idxDes] = array[idxDes], array[i]

# Ejecutar la funcion del algortimo
selectionSort(array)
print("Array Ordenado:")

for i in range(len(array)):
    print("%d" %array[i]),

