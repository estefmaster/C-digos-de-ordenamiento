import random
import time

def heap_sort_iterativo(lista):
    """Implementación de Heap Sort sin usar recursión"""
    arr = lista.copy()
    n = len(arr)

    # 1. Construir el Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_iterativo(arr, n, i)

    # 2. Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        # Movemos la raíz actual (el más grande) al final
        arr[i], arr[0] = arr[0], arr[i]
        # Aplicamos heapify en el montón reducido
        heapify_iterativo(arr, i, 0)
        
    return arr

def heapify_iterativo(arr, n, i):
    """Mantiene la propiedad de Max Heap usando un bucle while"""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  # Movemos el índice para seguir bajando en el árbol
        else:
            break

def main():
    # Usamos una f-string con formato profesional
    print(f"{' HEAP SORT ITERATIVO ':=^40}")
    
    datos = [random.randint(1, 10000) for _ in range(1000)]
    
    t_inicio = time.perf_counter()
    ordenada = heap_sort_iterativo(datos)
    t_fin = time.perf_counter()

    print(f"Resultado: {'✅ Correcto' if ordenada == sorted(datos) else '❌ Error'}")
    print(f"Tiempo: {t_fin - t_inicio:.6f} segundos")
    print(f"Top 3: {ordenada[:3]} ... {ordenada[-3:]}")

if __name__ == "__main__":
    main()
