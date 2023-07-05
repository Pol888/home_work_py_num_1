# Задача 1:
a = 2  # = int(input())
b = 2  # = int(input())
c = 2  # = int(input())
combinations = [a + b > c, b + c > a, c + a > b]

if False in combinations:
    print("Треугольник не существует")
else:
    print("Треугольник существует")
    if a == b == c:
        print("Он равносторонний")
    elif a == b or a == c or b == c:
        print("Он равнобедренный")
    else:
        print("Он разносторонний")

# Задача 2
divisor_counter = 0
while True:
    number = int(input('Введите число от 1 до 100000\n'))
    if number < 1 or number > 100000:
        print("Число не соответствует желаемым параметрам")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                divisor_counter += 1
        if divisor_counter > 2:
            print("Число составное")
            break
        else:
            print("Число простое")
            break

# Задача 3
from random import randint

attempt_counter = 1
num = randint(0, 1000)
print(f"Попробуйте отгадать число от 0 до 1000 c 10 попыток")
while True:
    answer = int(input(f"Попытка № {attempt_counter}\n"))
    if answer < num:
        print("Загаданное число больше")
        attempt_counter += 1
    elif answer > num:
        print("Загаданное число меньше")
        attempt_counter += 1
    else:
        print("Вы угадали число")
        break
    if attempt_counter == 11:
        print("Попытки закончились, вы лузер")
        break
