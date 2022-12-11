import java.util.Arrays;

//1. Buscar el número menor en mi array
//2. Crear dos subArrays para llevar el control de mi algoritmo
//3. Imprimir el resultado del ordenamiento.
public class selectionSort {

    // Ciclo que recorre todo el array y busca el valor mínimo
    static void selectionSort(int[] numeros) {
        int n = numeros.length;
        for (int i = 0; i < n - 1; i++) {
            int numMenor = i;
            for (int j = i + 1; j < n; j++) {
                if (numeros[numMenor] > numeros[j]) {
                    numMenor = j;
                }
            }
            int temp = numeros[i];
            numeros[i] = numeros[numMenor];
            numeros[numMenor] = temp;
            System.out.println("El Array como está quedando es: " + Arrays.toString(numeros));
        }
    }

    public static void main(String[] args) {
        int[] numeros = { 20, 5, 21, 6, 23, 7, 34, 999, 68 };
        selectionSort(numeros);
        System.out.println("El array ordenado es: " + Arrays.toString(numeros));
    }

}
