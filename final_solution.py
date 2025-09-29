#!/usr/bin/env python3
"""
Решение задачи о минимальном делителе для префиксов массива.

Задача:
- Функция minD(x) возвращает минимальный простой делитель числа x (minD(1) = 0)
- Функция f(x, y) = minD(xy / gcd(x, y)²)
- Для каждого префикса массива вычислить сумму f(a_i, a_j) для всех пар i < j

Алгоритм:
1. Реализуем функцию поиска минимального простого делителя
2. Реализуем функцию f(x, y)
3. Используем оптимизированный подход: при добавлении нового элемента
   в префикс добавляем только новые пары с этим элементом
"""

import math
from typing import List

def get_min_divisor(x: int) -> int:
    """
    Возвращает минимальный простой делитель числа x.
    
    Args:
        x: целое число
        
    Returns:
        минимальный простой делитель x, или 0 если x = 1
        
    Examples:
        >>> get_min_divisor(12)
        2
        >>> get_min_divisor(35)
        5
        >>> get_min_divisor(179)
        179
        >>> get_min_divisor(1)
        0
    """
    if x == 1:
        return 0
    
    if x <= 1:
        return x
    
    # Проверяем делимость на числа от 2 до sqrt(x)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    
    # Если не нашли делитель, то x - простое число
    return x

def gcd(a: int, b: int) -> int:
    """
    Вычисляет наибольший общий делитель двух чисел используя алгоритм Евклида.
    
    Args:
        a, b: целые числа
        
    Returns:
        НОД(a, b)
    """
    while b:
        a, b = b, a % b
    return a

def f_function(x: int, y: int) -> int:
    """
    Вычисляет f(x, y) = minD(xy / gcd(x, y)²).
    
    Args:
        x, y: целые числа
        
    Returns:
        minD(xy / gcd(x, y)²)
        
    Examples:
        >>> f_function(12, 35)
        2
        >>> f_function(6, 8)
        2
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
    
    Использует оптимизированный подход: при добавлении нового элемента в префикс
    добавляем только новые пары с этим элементом, избегая пересчета всех пар.
    
    Args:
        arr: массив целых чисел длины n
        
    Returns:
        список из n элементов, где i-й элемент - сумма f(a_j, a_k) для всех пар j < k <= i
        
    Time Complexity: O(n²) - для каждого префикса рассматриваем все пары
    Space Complexity: O(1) дополнительной памяти (не считая результат)
    
    Examples:
        >>> solve_prefix_sums([6, 8])
        [0, 2]
        >>> solve_prefix_sums([12, 35, 179])
        [0, 2, 9]
    """
    n = len(arr)
    result = []
    current_sum = 0
    
    # Для каждого префикса длины i (i от 1 до n)
    for i in range(1, n + 1):
        # Добавляем пары, где второй элемент - новый (arr[i-1])
        new_element = arr[i - 1]
        for j in range(i - 1):
            current_sum += f_function(arr[j], new_element)
        
        result.append(current_sum)
    
    return result

def solve_naive(arr: List[int]) -> List[int]:
    """
    Наивное решение: для каждого префикса пересчитываем все пары.
    
    Используется для проверки корректности оптимизированного решения.
    
    Args:
        arr: массив целых чисел
        
    Returns:
        список сумм для каждого префикса
        
    Time Complexity: O(n³)
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

def verify_solution(arr: List[int]) -> bool:
    """
    Проверяет корректность решения, сравнивая оптимизированную и наивную версии.
    
    Args:
        arr: массив для проверки
        
    Returns:
        True если решения совпадают, False иначе
    """
    result_opt = solve_prefix_sums(arr)
    result_naive = solve_naive(arr)
    return result_opt == result_naive

def main():
    """Основная функция с примерами использования"""
    print("=== Решение задачи о минимальном делителе ===\n")
    
    # Тестовые примеры
    test_cases = [
        ([12, 35, 179], "Пример из условия"),
        ([6, 8, 12, 15], "Смешанные числа"),
        ([1, 2, 3, 4, 5], "Последовательные числа"),
        ([17, 23, 29, 31], "Простые числа"),
        ([4, 9, 16, 25], "Квадраты"),
    ]
    
    for arr, description in test_cases:
        print(f"{description}: {arr}")
        
        # Проверяем корректность
        if verify_solution(arr):
            result = solve_prefix_sums(arr)
            print(f"Результат: {result}")
        else:
            print("ОШИБКА: оптимизированное и наивное решения не совпадают!")
        print()
    
    # Демонстрация работы функций
    print("=== Демонстрация функций ===")
    print(f"minD(12) = {get_min_divisor(12)}")
    print(f"minD(35) = {get_min_divisor(35)}")
    print(f"minD(179) = {get_min_divisor(179)}")
    print(f"minD(1) = {get_min_divisor(1)}")
    print()
    
    print(f"f(12, 35) = {f_function(12, 35)}")
    print(f"  Объяснение: gcd(12, 35) = 1, поэтому f = minD(12*35/1) = minD(420) = 2")
    print()
    
    print(f"f(6, 8) = {f_function(6, 8)}")
    print(f"  Объяснение: gcd(6, 8) = 2, поэтому f = minD(6*8/4) = minD(12) = 2")

if __name__ == "__main__":
    main()