# Найти максимальную цифру в числе

num = int(input("Введите число: "))
print(f'Вы ввели число {num}')

num_lst = [int(x) for x in list(str(num))]
num_max = max(num_lst)
print(f'Цифра - {num_max} максимальная в числе {num}')