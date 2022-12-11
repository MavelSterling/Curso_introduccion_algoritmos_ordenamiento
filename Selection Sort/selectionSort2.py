# 1. Buscar el numero menor en mi array
# 2. Crear dos subarrays para llevar el control de mi algoritmo
# 3. devolver los datos del array ordenados
import sys
def selectionSort(array):
    
    # Recorre todo nuestro array
    for i in range(len(array)):
        print(array)
        #Encontrar el menor dato del array desordenado
        #Auxiliar de el array desordenado
        idxDesordenado = i 
        
        for j in range(i+1, len(array)):
            if array[idxDesordenado] > array[j]:
                idxDesordenado = j

        # cuando encontramos el minimo elemento, lo cambiamos por el primer valor de nuestro array desordenado
        array[i], array[idxDesordenado] = array[idxDesordenado], array[i]


def main():

    array = [3,124,412,13,235,2,323,3,212,1,25,5,3,323,6,3]
    selectionSort(array)
    
    print("Array ordenado: ")
    
    for i in range(len(array)):
        print("%d"%array[i])

if __name__ == "__main__":
    main()