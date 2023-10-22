'''Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j

Входные данные
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Выходные данные
Выведите результат. Решение оформите в виде функции SwapColumns (A, i, j).'''
fin = open('input.txt')
a = []
n, m = map(int, fin.readline().split())
for i in range(n):
    s = list(map(int, fin.readline().split()))
    a.append(s)
k, j = map(int, fin.readline().split())
for i in range(n):
    a[i][k], a[i][j] = a[i][j], a[i][k]
for i in range(n):
    print(*a[i])

fin.close()