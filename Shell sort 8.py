# Shell Sort Algorithm Implementation
import random
import time

def create_random_data(length=1000):
    """Generates a list of random integers for testing."""
    return [random.randint(1, 10000) for _ in range(length)]

def execute_shell_sort(data):
    """Core Shell Sort logic using the original Shell sequence."""
    working_list = data.copy()
    size = len(working_list)
    
    # Initialize the gap
    interval = size // 2
    
    while interval > 0:
        for current_pos in range(interval, size):
            val_to_insert = working_list[current_pos]
            cursor = current_pos
            
            # Shift elements until the correct spot is found
            while cursor >= interval and working_list[cursor - interval] > val_to_insert:
                working_list[cursor] = working_list[cursor - interval]
                cursor -= interval
                
            working_list[cursor] = val_to_insert
        
        # Reduce the gap for the next pass
        interval //= 2
        
    return working_list

def run_process():
    print("--- ALGORITMO: SHELL SORT ---")
    
    # Data generation phase
    sample_size = 1000
    raw_list = create_random_data(sample_size)
    print(f"Entrada inicial (10 items): {raw_list[:10]}")
    
    # Sorting phase with performance timing
    start_mark = time.perf_counter()
    processed_list = execute_shell_sort(raw_list)
    end_mark = time.perf_counter()
    
    # Validation phase
    reference_list = sorted(raw_list)
    
    print(f"\nResultado final (10 items): {processed_list[:10]}")
    print(f"Duración: {end_mark - start_mark:.6f} s")
    print(f"¿Éxito en ordenamiento?: {processed_list == reference_list}")
    print(f"Rango: [{processed_list[0]} - {processed_list[-1]}]")

if __name__ == "__main__":
    run_process()
