import math
from typing import List

def sieve_of_eratosthenes(max_num: int) -> List[int]:
    """
    Находит все простые числа до max_num используя решето Эратосфена.
    """
    if max_num < 2:
        return []
    
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, max_num + 1) if is_prime[i]]

def get_min_divisor(x: int) -> int:
    """
    Возвращает минимальный простой делитель числа x.
    minD(1) = 0 по условию задачи.
    """
    if x == 1:
        return 0
    
    if x <= 1:
        return x
    
    # Проверяем делимость на простые числа до sqrt(x)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    
    # Если не нашли делитель, то x - простое число
    return x

def gcd(a: int, b: int) -> int:
    """
    Вычисляет наибольший общий делитель двух чисел.
    """
    while b:
        a, b = b, a % b
    return a

def f_function(x: int, y: int) -> int:
    """
    Вычисляет f(x, y) = minD(xy / gcd(x, y)²)
    """
    if x == 0 or y == 0:
        return 0
    
    gcd_xy = gcd(x, y)
    if gcd_xy == 0:
        return 0
    
    # Вычисляем xy / gcd(x, y)²
    numerator = x * y
    denominator = gcd_xy * gcd_xy
    
    if numerator % denominator != 0:
        # Это не должно происходить по свойствам НОД
        return 0
    
    result = numerator // denominator
    return get_min_divisor(result)

def solve_prefix_sums(arr: List[int]) -> List[int]:
    """
    Решает задачу: для каждого префикса массива вычисляет сумму f(a_i, a_j) для всех пар i < j.
    
    Args:
        arr: массив целых чисел
        
    Returns:
        список сумм для каждого префикса
    """
    n = len(arr)
    result = []
    
    for prefix_len in range(1, n + 1):
        total_sum = 0
        
        # Перебираем все пары (i, j) где i < j < prefix_len
        for i in range(prefix_len):
            for j in range(i + 1, prefix_len):
                total_sum += f_function(arr[i], arr[j])
        
        result.append(total_sum)
    
    return result

def solve_optimized(arr: List[int]) -> List[int]:
    """
    Оптимизированная версия решения.
    Вместо пересчета всех пар для каждого префикса,
    добавляем новые пары при увеличении префикса.
    """
    n = len(arr)
    result = []
    current_sum = 0
    
    for prefix_len in range(1, n + 1):
        # Добавляем пары, где j = prefix_len - 1 (новый элемент)
        new_element = arr[prefix_len - 1]
        for i in range(prefix_len - 1):
            current_sum += f_function(arr[i], new_element)
        
        result.append(current_sum)
    
    return result

# Примеры использования
if __name__ == "__main__":
    # Тестовые примеры
    test_cases = [
        [12, 35, 179],
        [6, 8, 12, 15],
        [1, 2, 3, 4, 5],
        [17, 23, 29, 31]  # простые числа
    ]
    
    for i, arr in enumerate(test_cases):
        print(f"Тест {i + 1}: {arr}")
        result = solve_optimized(arr)
        print(f"Результат: {result}")
        print()
    
    # Проверка отдельных функций
    print("Проверка функций:")
    print(f"minD(12) = {get_min_divisor(12)}")  # должно быть 2
    print(f"minD(35) = {get_min_divisor(35)}")  # должно быть 5  
    print(f"minD(179) = {get_min_divisor(179)}")  # должно быть 179
    print(f"minD(1) = {get_min_divisor(1)}")  # должно быть 0
    
    print(f"\nf(12, 35) = {f_function(12, 35)}")
    print(f"f(35, 179) = {f_function(35, 179)}")