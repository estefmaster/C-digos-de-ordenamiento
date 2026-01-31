import random
import time

def counting_sort_estable(lista):
    """Implementación clásica con posiciones acumuladas"""
    if not lista:
        return []

    # 1. Definir el rango
    min_val, max_val = min(lista), max(lista)
    rango = max_val - min_val + 1
    
    # 2. Frecuencias y Posiciones
    conteo = [0] * rango
    salida = [0] * len(lista)

    # Contar ocurrencias (ajustando por el valor mínimo)
    for num in lista:
        conteo[num - min_val] += 1

    # Modificar conteo para que tenga las posiciones reales (Suma acumulada)
    for i in range(1, len(conteo)):
        conteo[i] += conteo[i - 1]

    # 3. Construir el array de salida (de atrás hacia adelante para estabilidad)
    for i in range(len(lista) - 1, -1, -1):
        num = lista[i]
        posicion = conteo[num - min_val] - 1
        salida[posicion] = num
        conteo[num - min_val] -= 1

    return salida

def benchmark():
    # Generación compacta
    n = 1000
    datos = [random.randint(1, 10000) for _ in range(n)]
    
    print(f"🚀 Ordenando {n} elementos con Counting Sort Estable...")
    
    t_inicio = time.perf_counter()
    resultado = counting_sort_estable(datos)
    t_fin = time.perf_counter()
    
    # Resultados
    print("-" * 30)
    print(f"✅ Éxito: {resultado == sorted(datos)}")
    print(f"⏱️ Tiempo: {t_fin - t_inicio:.6f} segundos")
    print(f"📊 Rango: {min(resultado)} a {max(resultado)}")

if __name__ == "__main__":
    benchmark()
