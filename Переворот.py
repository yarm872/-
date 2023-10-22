'''Дан массив N × M. Требуется повернуть его по часовой стрелке на 90 градусов.

Входные данные
На первой строке даны натуральные числа N и M (1 ≤ N, M ≤ 50). На следующих N строках записано по M неотрицательных чисел, не превышающих 109 – сам массив.

Выходные данные
Выведите повернутый массив в формате входных данных.'''
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

print(m, n)
for i in range(m):
    for j in range(n):
        print(b[i][j], end=' ')
    print()