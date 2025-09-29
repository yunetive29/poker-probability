import math
from typing import List

def minD(x: int) -> int:
    """
    Функция минимального простого делителя.
    minD(1) = 0, minD(x) = минимальное простое число, на которое делится x.
    """
    if x == 1:
        return 0
    if x == 2:
        return 2
    if x % 2 == 0:
        return 2
    
    # Проверяем нечетные делители до sqrt(x)
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return i
    
    # Если не нашли делителей, то x - простое число
    return x

def gcd(a: int, b: int) -> int:
    """Вычисление наибольшего общего делителя."""
    while b:
        a, b = b, a % b
    return a

def f(x: int, y: int) -> int:
    """
    Функция f(x,y) = minD(xy / gcd(x,y)²)
    """
    g = gcd(x, y)
    if g == 0:
        return 0
    numerator = x * y
    denominator = g * g
    if numerator % denominator != 0:
        return 0
    return minD(numerator // denominator)

def solve_prefix_sums(arr: List[int]) -> List[int]:
    """
    Для каждого префикса массива вычисляет сумму f(a_i, a_j) для всех i < j.
    """
    n = len(arr)
    result = []
    
    for prefix_len in range(1, n + 1):
        total_sum = 0
        # Вычисляем сумму f(a_i, a_j) для всех i < j в текущем префиксе
        for i in range(prefix_len):
            for j in range(i + 1, prefix_len):
                total_sum += f(arr[i], arr[j])
        result.append(total_sum)
    
    return result

def solve_prefix_sums_optimized(arr: List[int]) -> List[int]:
    """
    Оптимизированная версия с использованием накопления.
    """
    n = len(arr)
    result = []
    current_sum = 0
    
    for i in range(n):
        # Добавляем f(a_i, a_j) для всех j < i
        for j in range(i):
            current_sum += f(arr[j], arr[i])
        result.append(current_sum)
    
    return result

# Тестирование
def test_functions():
    """Тесты для проверки корректности функций."""
    
    # Тесты для minD
    assert minD(1) == 0
    assert minD(2) == 2
    assert minD(12) == 2
    assert minD(35) == 5
    assert minD(179) == 179
    assert minD(17) == 17  # простое число
    
    # Тесты для f
    # f(12, 35) = minD(12*35 / gcd(12,35)²)
    # gcd(12, 35) = 1, поэтому f(12, 35) = minD(12*35) = minD(420)
    # 420 = 2² * 3 * 5 * 7, minD(420) = 2
    assert f(12, 35) == 2
    
    print("Все тесты пройдены!")

def main():
    """Основная функция для демонстрации работы."""
    test_functions()
    
    # Пример использования
    arr = [12, 35, 179, 6, 10]
    print(f"Массив: {arr}")
    
    # Решение с оптимизацией
    result = solve_prefix_sums_optimized(arr)
    print(f"Результат для каждого префикса: {result}")
    
    # Детальный вывод для понимания
    print("\nДетальный расчет:")
    for i in range(len(arr)):
        prefix = arr[:i+1]
        print(f"Префикс {i+1}: {prefix}")
        
        total = 0
        for j in range(i+1):
            for k in range(j+1, i+1):
                f_val = f(prefix[j], prefix[k])
                print(f"  f({prefix[j]}, {prefix[k]}) = {f_val}")
                total += f_val
        print(f"  Сумма: {total}")
        print()

if __name__ == "__main__":
    main()