'''Дан квадратный массив. Поверните его на 90 градусов по часовой стрелке. Результат запишите в этот же массив, вспомогательный массив использовать нельзя.

Входные данные
Вводятся одно число n - размер квадратного массива, а затем сам массив размером n×n

Выходные данные
Выведите результат на экран, разделяя числа одним пробелом.'''
fin = open('input.txt')
a = []
b = []
n = int(fin.readline())
for i in range(n):
    b.append([0] * n)
for i in range(n):
    s = list(map(int, fin.readline().split()))
    a.append(s)
for i in range(n):
    for j in range(n):
        b[j][i] = a[i][j]
for i in range(n):
    for j in range(n // 2):
        b[i][j], b[i][n - j - 1] = b[i][n - j - 1], b[i][j]

for i in range(n):
    print(*b[i])

fin.close()