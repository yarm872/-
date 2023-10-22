'''Дан двумерный массив размером n×n. Транспонируйте его и результат запишите в этот же массив. Вспомогательный массив
использовать нельзя. Решение оформите в виде функции Transpose (A).'''
fin = open('input.txt')
a = []
n = int(fin.readline())
for i in range(n):
    s = list(map(int, fin.readline().split()))
    a.append(s)
for i in range(n):
    for j in range(i):
        a[i][j], a[j][i] = a[j][i], a[i][j]
for i in range(n):
    print(*a[i])

fin.close()