private static void selectionSort(Integer[] array) {
		for(int i = 0; i < array.length - 1; i++) {			
			int min = array[i];
			int index = i;
			for(int j = i+1; j < array.length; j++) {	
				if(array[j] < min) {
					min = array[j];
					index = j;
				}
			}
			swap(array,i,index);
			List arr = Arrays.asList(array);		
			System.out.println("Iteración "+ (i+1) +": "+arr);
		}
	}
	
	private static void swap(Integer[] array, int origin, int destinity) {
		int tempValue = array[origin];
		array[origin] = array[destinity];
		array[destinity] = tempValue;
	}