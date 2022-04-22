# Найти количество цифр 5 в числе

num = int(input("Введите число: "))
print(f'Вы ввели число {num}')

num_lst = list(str(num))

num_five = 0
for i in num_lst:
    if i == '5':    num_five += 1

print(f'В числе {num} {num_five} 5-кa/и')