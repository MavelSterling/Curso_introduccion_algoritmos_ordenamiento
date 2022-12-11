#1. Comenzar a hacer comparaciones de elementos adyacentes
#2.  Repetir hasta tener una pasada completa sin ningun swap

from datetime import datetime

def bubbleSort(array):
	n = len(array) # cuantos numeros hay en el arreglo

	for i in range(n): # recorre todos los elementos del array
		swap = False
		print(array)

         # se comienza en 0 hasta n(numero de elementos en el array)
         # i (posicion en el cual se esta en el array) 

		for j in range(0, n-i-1): 
			if array[j] > array[j+1] :
				swap = True
				array[j], array[j+1] = array[j+1], array[j] # cambia si el valor de j es mayor que el valor de la posicion j+1
		if not swap :
            		break



array=[190,1200, 1,2,4,55,1000,6,800]

bubbleSort(array)      

print("El arreglo ordenado de forma Ascendete es:")

for i in range(len(array)):
    print("%d"%array[i]),




array = [6209,2663,4132,2074,4603,3735,5169,4627,6290,76,
5259,4356,3263,6311,3496,1010,5382,2042,427,6724,5467,5529,
4844,6426,524,6032,6275,4174,3184,6492,5851,4803,2356,6411,
2543,1199,2043,1603,17,6844,2472,4084,1112,339,4514,3694,496,
952,6390,4049,1986,1909,2728,883,2314,1813,1767,2008,2273,2254,
5660,2088,2969,4450,413,3688,607,2364,581,4644,1622,2117,2088,5867]

tiempoInicial = datetime.now()
bubbleSort(array)

print ("El arreglo ordenado de forma Ascendete es:")
for i in range(len(array)):
	print("%d"%array[i])
	
print (datetime.now() - tiempoInicial),
