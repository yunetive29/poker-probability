#!/usr/bin/env python3

import sys
sys.path.append('/workspace')
from min_divisor_solution import get_min_divisor, f_function, solve_optimized, solve_prefix_sums

def test_min_divisor():
    """Тестирует функцию минимального делителя"""
    print("=== Тестирование minD(x) ===")
    
    test_cases = [
        (1, 0),
        (2, 2),
        (3, 3),
        (4, 2),
        (12, 2),
        (35, 5),
        (179, 179),
        (6, 2),
        (15, 3),
        (100, 2),
        (17, 17),
        (25, 5)
    ]
    
    for x, expected in test_cases:
        result = get_min_divisor(x)
        status = "✓" if result == expected else "✗"
        print(f"minD({x}) = {result} (ожидалось {expected}) {status}")
        if result != expected:
            print(f"  ОШИБКА: неверный результат!")

def test_f_function():
    """Тестирует функцию f(x, y)"""
    print("\n=== Тестирование f(x, y) ===")
    
    # Некоторые тестовые случаи
    test_cases = [
        (12, 35),  # gcd(12, 35) = 1, f = minD(12*35/1) = minD(420) = 2
        (6, 8),    # gcd(6, 8) = 2, f = minD(48/4) = minD(12) = 2
        (12, 8),   # gcd(12, 8) = 4, f = minD(96/16) = minD(6) = 2
        (15, 12),  # gcd(15, 12) = 3, f = minD(180/9) = minD(20) = 2
        (17, 23),  # gcd(17, 23) = 1, f = minD(391/1) = minD(391) = 17
    ]
    
    for x, y in test_cases:
        result = f_function(x, y)
        print(f"f({x}, {y}) = {result}")
        print(f"  gcd({x}, {y}) = {gcd(x, y)}")
        print(f"  xy/gcd² = {x * y} / {gcd(x, y)**2} = {(x * y) // (gcd(x, y)**2)}")
        print(f"  minD({(x * y) // (gcd(x, y)**2)}) = {result}")

def gcd(a, b):
    """Вспомогательная функция для НОД"""
    while b:
        a, b = b, a % b
    return a

def test_prefix_sums():
    """Тестирует решение для префиксов"""
    print("\n=== Тестирование префиксов ===")
    
    # Простой тест
    arr = [6, 8]
    result_opt = solve_optimized(arr)
    result_naive = solve_prefix_sums(arr)
    
    print(f"Массив: {arr}")
    print(f"Оптимизированное решение: {result_opt}")
    print(f"Наивное решение: {result_naive}")
    
    if result_opt == result_naive:
        print("✓ Результаты совпадают")
    else:
        print("✗ Результаты не совпадают!")
    
    # Подробный разбор для [6, 8]
    print("\nПодробный разбор для [6, 8]:")
    print("Префикс длины 1: [6] - нет пар, сумма = 0")
    print("Префикс длины 2: [6, 8] - одна пара (6, 8)")
    print(f"  f(6, 8) = minD(6*8/gcd(6,8)²) = minD(48/4) = minD(12) = 2")
    print(f"  Сумма = 0 + 2 = 2")

def test_edge_cases():
    """Тестирует граничные случаи"""
    print("\n=== Граничные случаи ===")
    
    # Пустой массив (не должно происходить по условию)
    # Массив из одного элемента
    arr1 = [42]
    result1 = solve_optimized(arr1)
    print(f"[42]: {result1} (должно быть [0])")
    
    # Массив из одинаковых элементов
    arr2 = [5, 5, 5]
    result2 = solve_optimized(arr2)
    print(f"[5, 5, 5]: {result2}")
    
    # Массив с единицами
    arr3 = [1, 2, 3]
    result3 = solve_optimized(arr3)
    print(f"[1, 2, 3]: {result3}")

if __name__ == "__main__":
    test_min_divisor()
    test_f_function()
    test_prefix_sums()
    test_edge_cases()
    
    print("\n=== Итоговые тесты ===")
    
    # Тест из условия задачи
    print("Проверяем примеры из условия:")
    print(f"minD(12) = {get_min_divisor(12)} (ожидалось 2)")
    print(f"minD(35) = {get_min_divisor(35)} (ожидалось 5)")
    print(f"minD(179) = {get_min_divisor(179)} (ожидалось 179)")
    print(f"minD(1) = {get_min_divisor(1)} (ожидалось 0)")
    
    print("\nВсе тесты завершены!")