# lesson_2_task_2.py
# Задача: определить, является ли год високосным (высокосный — если делится на 4 без остатка).

def is_year_leap(year):
    return year % 4 == 0

year = 2024  # можно подставить любой год
year = 2023
result = is_year_leap(year)

print(f"год {year}: {result}")