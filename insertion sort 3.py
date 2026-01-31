import random
import time

def binary_search(arr, val, start, end):
    """Encuentra la posición donde debería insertarse 'val'"""
    if start == end:
        return start if arr[start] > val else start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def insertion_sort_binario(lista):
    """Versión optimizada de Insertion Sort usando búsqueda binaria"""
    arr = lista.copy()
    for i in range(1, len(arr)):
        val = arr[i]
        # Usamos búsqueda binaria para hallar el lugar exacto
        j = binary_search(arr, val, 0, i - 1)
        
        # Desplazamos los elementos a la derecha en una sola línea (Slicing)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        
    return arr

def main():
    print("--- BINARY INSERTION SORT ---")
    numeros = [random.randint(1, 10000) for _ in range(1000)]
    
    start = time.perf_counter()
    resultado = insertion_sort_binario(numeros)
    end = time.perf_counter()
    
    print(f"¿Orden correcto?: {'SÍ' if resultado == sorted(numeros) else 'NO'}")
    print(f"Tiempo: {end - start:.5f} segundos")
    print(f"Muestra: {resultado[:5]} ... {resultado[-5:]}")

if __name__ == "__main__":
    main()
