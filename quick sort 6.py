import random
import time
import sys

# Aumentamos el límite de recursión por si acaso, 10k números es un reto
sys.setrecursionlimit(15000)

def quick_sort_hoare(arr, low, high):
    """
    Versión eficiente que no crea listas nuevas, 
    sino que mueve los elementos dentro de la misma lista.
    """
    if low < high:
        # p es el índice del pivote ya posicionado
        p = particion(arr, low, high)
        quick_sort_hoare(arr, low, p)
        quick_sort_hoare(arr, p + 1, high)

def particion(arr, low, high):
    """Esquema de partición de Hoare"""
    pivot = arr[(low + high) // 2] # Pivote en el centro para evitar casos lentos
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
            
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        if i >= j:
            return j
            
        # Intercambio (Swap) directo
        arr[i], arr[j] = arr[j], arr[i]

def main():
    n = 10000 # Los 10,000 que pediste
    print(f"--- QUICK SORT (HOARE PARTITION) | n={n} ---")
    
    # Generación
    datos = [random.randint(1, 100000) for _ in range(n)]
    
    # Ordenamiento
    inicio = time.perf_counter()
    quick_sort_hoare(datos, 0, len(datos) - 1)
    fin = time.perf_counter()
    
    # Verificación
    print(f"¿Ordenado correctamente?: {'SÍ' if datos == sorted(datos) else 'NO'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")
    print(f"Extremos: Mín {datos[0]} | Máx {datos[-1]}")

if __name__ == "__main__":
    main()
