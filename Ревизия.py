'''В связи с визитом Императора Палпатина было решено обновить состав дроидов в ангаре 32.
Из-за кризиса было решено новых дроидов не закупать, но выкинуть пару старых. Как известно, Палпатин не переносит дроидов
с маленькими серийными номерами, так что все, что требуется - найти среди них двух, у которых серийные номера наименьшие.

Входные данные
Первая строка входного файла содержит целое число N – количество дроидов. (2 ≤ N ≤ 1000), вторая строка – N целых чисел,
по модулю не превышающих 2*10^9 – номера дроидов



Выходные данные
Выведите два числа: первым – последний по величине из номеров дроидов (такого следует утилизировать в первую очередь),
а вторым – предпоследний.'''
n=int(input())
a=list(map(int,input().split()))
m1=a[0]
m2=a[1]
if m2<m1:
    m1,m2=m2,m1
for i in range(2,n):
    if a[i]<m1:
        m2=m1
        m1=a[i]
    elif a[i]<m2:
        m2=a[i]
print(m1,end=' ')
print(m2)