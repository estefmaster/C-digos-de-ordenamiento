import random
import time

def merge_sort_iterativo(lista):
    """
    Ordenamiento por mezcla de abajo hacia arriba (Bottom-Up).
    Evita la recursión para manejar grandes volúmenes de datos.
    """
    n = len(lista)
    res = lista.copy()
    ancho = 1
    
    while ancho < n:
        for i in range(0, n, ancho * 2):
            izq = i
            medio = min(i + ancho, n)
            der = min(i + 2 * ancho, n)
            
            # Combinación de sub-listas
            res[izq:der] = combinar(res[izq:medio], res[medio:der])
            
        ancho *= 2
    return res

def combinar(izquierda, derecha):
    """Mezcla dos arreglos manteniendo el orden ascendente."""
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    # Añadir elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ejecutar_analisis():
    # Configuración de la prueba
    cantidad_numeros = 10000
    rango_maximo = 50000
    
    print(f"--- PRUEBA DE RENDIMIENTO: {cantidad_numeros} NÚMEROS ---")
    
    # Generación de datos
    datos = [random.randint(1, rango_maximo) for _ in range(cantidad_numeros)]
    print(f"Primeros 5 números aleatorios: {datos[:5]}")
    
    # Medición de tiempo
    t_inicio = time.perf_counter()
    lista_final = merge_sort_iterativo(datos)
    t_fin = time.perf_counter()
    
    # Verificación de integridad
    es_valido = lista_final == sorted(datos)
    
    print("-" * 40)
    print(f"Estado de ordenamiento: {'CORRECTO' if es_valido else 'ERROR'}")
    print(f"Tiempo total: {t_fin - t_inicio:.6f} segundos")
    print(f"Menor valor: {lista_final[0]}")
    print(f"Mayor valor: {lista_final[-1]}")
    print("-" * 40)

if __name__ == "__main__":
    ejecutar_analisis()
