num = int(input("Введите число: "))
print(f'Вы ввели число {num}')

num_s = list(str(num))
num_s = sum([int(x) for x in num_s])


print(f"Сумма цифр числа {num}: {num_s}")