import math

num = int(input("Введите число: "))
print(f'Вы ввели число {num}')

num_p = list(str(num))
num_p = math.prod([int(x) for x in num_p])


print(f"Произведение цифр числа {num}: {num_p}")