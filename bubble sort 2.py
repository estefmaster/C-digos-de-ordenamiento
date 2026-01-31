import random
import time

def quick_sort(arr):
    """Implementación recursiva de Quick Sort (Divide y vencerás)"""
    if len(arr) <= 1:
        return arr
    
    # Elegimos un pivote (el elemento central)
    pivot = arr[len(arr) // 2]
    
    # Clasificamos los elementos en tres listas
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursión: ordenamos las partes y las unimos
    return quick_sort(left) + middle + quick_sort(right)

def ejecutar_prueba(cantidad=1000):
    # Generación elegante de lista
    datos = [random.randint(1, 10000) for _ in range(cantidad)]
    
    print(f"--- Reto de Ordenamiento: {cantidad} elementos ---")
    
    inicio = time.perf_counter() # Más preciso que time.time()
    resultado = quick_sort(datos)
    fin = time.perf_counter()
    
    # Validación rápida
    es_valido = resultado == sorted(datos)
    
    print(f"¿Ordenado correctamente?: {'✅' if es_valido else '❌'}")
    print(f"Tiempo récord: {fin - inicio:.6f} segundos")
    print(f"Top 5 menores: {resultado[:5]}")
    print(f"Top 5 mayores: {resultado[-5:]}")

if __name__ == "__main__":
    ejecutar_prueba()
