'''Дан список из N (N≤2∗10^5) элементов,которые принимают целые значения от 0 до 100.

Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.



Примечание

Сложность работы программы должна быть O(n). Использование встроенной сортировки(sort, sorted),
алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!'''
a=list(map(int,input().split()))
n=len(a)
b=[0]*101
n1=len(b)
for i in range(n):
      b[a[i]]+=1
for i in range(n1):
      if b[i]!=0:
            for j in range(b[i]):
                  print(i,end=' ')