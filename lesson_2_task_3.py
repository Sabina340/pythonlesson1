# lesson_2_task_3.py
# Функция для вычисления площади квадрата
# Если результат не целый — округляем вверх.

import math

def square(side):
    area = side * side
    return math.ceil(area)

side = 5.8

result = square(side)

print(f"Сторона квадрата: {side}, площадь: {result}")