'''Дан прямоугольный массив размером n×m. Поверните его на 90 градусов по часовой стрелке, записав результат в новый массив размером m×n.

Входные данные
Вводятся два числа n и m, затем массив размером n×m

Выходные данные
Выведите получившийся массив. Числа при выводе разделяйте одним пробелом.'''
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    b.append([0] * n)
for i in range(n):
    for j in range(m):
        b[j][n - 1 - i] = a[i][j]

for i in range(m):
    for j in range(n):
        print(b[i][j], end=' ')
    print()