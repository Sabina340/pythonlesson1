# lesson_2_task_4.py
# Функция fizz_buzz, которая печатает числа от 1 до n
# с заменой по правилам Fizz / Buzz / FizzBuzz.

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(17)