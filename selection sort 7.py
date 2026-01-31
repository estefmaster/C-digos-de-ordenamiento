import random
import time
from typing import List

class Sorter:
    """Clase para encapsular utilidades de ordenamiento y pruebas."""
    
    @staticmethod
    def generate_data(size: int = 1000, limit: int = 10000) -> List[int]:
        """Crea una lista de enteros aleatorios."""
        return [random.randint(1, limit) for _ in range(size)]

    @staticmethod
    def selection_sort(data: List[int]) -> List[int]:
        """
        Ordena la lista utilizando el algoritmo de selección.
        Complejidad temporal: O(n^2)
        """
        arr = data.copy()
        n = len(arr)
        
        for i in range(n):
            # Asumimos que el primero es el mínimo
            idx_min = i
            for j in range(i + 1, n):
                if arr[j] < arr[idx_min]:
                    idx_min = j
            
            # Intercambio elegante (Sustituye al min si se encontró uno menor)
            if idx_min != i:
                arr[i], arr[idx_min] = arr[idx_min], arr[i]
                
        return arr

def run_benchmark():
    # Configuración inicial
    SIZE = 1000
    dataset = Sorter.generate_data(SIZE)
    
    print("="*30)
    print(f"🚀 INICIANDO SELECTION SORT")
    print(f"Muestra: {SIZE} elementos")
    print("="*30)

    # Proceso de ordenamiento y medición
    start_clock = time.perf_counter()
    sorted_result = Sorter.selection_sort(dataset)
    end_clock = time.perf_counter()
    
    # Validación y métricas
    duration = end_clock - start_clock
    is_valid = sorted_result == sorted(dataset)
    
    print(f"✅ Estado: {'Ordenado' if is_valid else 'Error'}")
    print(f"⏱️ Tiempo: {duration:.4f} segundos")
    print("-" * 30)
    print(f"Primeros 5: {sorted_result[:5]}")
    print(f"Últimos  5: {sorted_result[-5:]}")
    print("="*30)

if __name__ == "__main__":
    run_benchmark()
