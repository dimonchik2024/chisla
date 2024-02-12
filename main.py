import random

def generate_numbers():
    numbers = [random.randint(1, 10) for _ in range(5)]
    print("Случайные числа:", numbers)
    user_sum = input("Введите сумму этих чисел: ")
    try:
        user_sum = int(user_sum)
        if user_sum == sum(numbers):
            print("Верно! Сумма чисел:", sum(numbers))
        else:
            print("Неверно. Правильная сумма:", sum(numbers))
    except ValueError:
        print("Пожалуйста, введите корректное число.")

generate_numbers()