import math

# Задача 1
# n = list(map(int, input('n = ').split()))
# a = len(n)//2
# if sum(n[:a]) == sum(n[a:]):
#     print('Счастливый')
# else:
#     print('Несчасный')


# Задача 2
# n = int(input("n = "))
# a = str(n)
# if a[::] == a[::-1]:
#     print("Число является палинромом")
# else:
#     print("Число не является палинромом")

# Задача 3
# r = 4
# x, y = map(float, input("Ведите координаты х и y: ").split())
# c = math.sqrt(x**2 + y**2)
# if c <= r:
#     print("Точка лежит внутри круга")
# else:
#     print("Точка не лежит внутри круга")

# Задача 4
# odd = []
# n = list(map(int, input('n = ').split()))
# for i in n:
#     if i % 2 != 0:
#         odd.append(i)
# print("Нечетных чисе в списке: ", len(odd))

# Задача 5
# c = []
# a = list(map(int, input('n = ').split()))
# for i in a:
#     c.append(i ** 2)
# print(a + c)

# Задача 6
# a = list(map(int, input('n = ').split()))
# print(f"Список зарплаты: {a}, средняя зарплата ровна: {sum(a)//12} ")

# Задача 7
a = list(map(int, input('a = ').split()))
b = list(map(int, input('b = ').split()))
c = list(map(int, input('c = ').split()))
d = list(map(int, input('d = ').split()))
total = a + b + c + d
print(f"{a}\n{b}\n{c}\n{d}\nСумма матрицы ровна:{sum(total)}")



