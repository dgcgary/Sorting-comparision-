#David Garcia Cruz - 2024115575
#Rodrigo Arce Bastos - 2024115582

import random
import time
import csv  

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)




def measure_time(sort_function, arr, *args):
    start_time = time.time()
    sort_function(arr, *args)
    end_time = time.time()
    return end_time - start_time


sizes = [1000, 2000, 3000, 4000, 5000]
results = {}

for size in sizes:
    total_time = 0
    arr = [random.randint(0, 100000) for _ in range(size)]
    print(size)
    
    for _ in range(10):  
        total_time += measure_time(bubble_sort, arr.copy())  
    average_time = total_time / 10
    results[size] = average_time

    total_time_quick = 0
    for _ in range(10):
        total_time_quick += measure_time(quickSort, arr.copy(), 0, len(arr) - 1)  
    average_time_quick = total_time_quick / 10
    results[size] = (average_time, average_time_quick)  


with open('resultados_bubble_sort_quick_sort.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tamaño", "Tiempo Promedio Bubble Sort (segundos)", "Tiempo Promedio Quick Sort (segundos)"])  
    for size, (avg_time_bubble, avg_time_quick) in results.items():
        writer.writerow([size, avg_time_bubble, avg_time_quick])  

print("Tiempos de ejecución promedio para Bubble Sort y Quick Sort guardados en resultados_bubble_sort_quick_sort.csv")




"""  
Preguntas  
a. ¿Cuál algoritmo es más rápido y por qué?
    El algoritmo de Quick Sort es mas rapido, ya que su tiempo de ejecucion es menor a Bubble Sort, esto se debe a que Quick Sort se basa en la tecnica de divide y conquista,
    mientras que Bubble Sort se basa en la tecnica de comparacion y intercambio.  



b. ¿El tiempo de ejecución será el mismo si la implementación del
algoritmo es iterativa o recursiva?
    No, el tiempo de ejecucion no sera el mismo, ya que la version recursiva divide el problema en subproblemas mas pequeños, mientras que la version iterativa no. 


c. ¿Es posible que exista un algoritmo de ordenamiento que sea muy
eficiente en consumo de recursos pero que a la vez sea relativamente
rápido?
    Si, es posible que exista un algoritmo de ordenamiento que sea muy eficiente en consumo de recursos pero que a la vez sea relativamente rapido.


d. Suponga que se planea ejecutar el algoritmo en un sistema
computacional con extremadamente bajos recursos de memoria. ¿Cuál
de los dos algoritmos de ordenamiento escogería y por qué?
    La complejidad espacial de Bubble Sort es O(1), ya que no requiere de memoria adicional para su ejecucion. 
    Mientras que la complejidad espacial de Quick Sort es O(log n), ya que requiere de memoria adicional para almacenar los subproblemas.
    Por lo tanto, si se planea ejecutar el algoritmo en un sistema computacional con extremadamente bajos recursos de memoria, se escogeria Bubble Sort.
    Mientras que si se planea ejecutar el algoritmo en un sistema computacional con recursos de memoria suficientes, se escogeria Quick Sort, ya que su tiempo de ejecucion es menor.









"""