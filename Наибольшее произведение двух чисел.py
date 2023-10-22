'''Дан список, заполненный произвольными целыми числами по модулю не превосходящими 106. Найдите в этом списке
два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.

Решение должно иметь сложность O(n), где n - размер списка.'''
a = list(map(int, input().split()))
n = len(a)
ma1 = a[0]
ma2 = a[0]
mi1 = a[0]
mi2 = a[0]

for i in range(1, n):
    if a[i] > ma1:
        ma2 = ma1
        ma1 = a[i]




    elif a[i] > ma2:
        ma2 = a[i]

    if a[i] < mi1:
        mi2 = mi1
        mi1 = a[i]


    elif a[i] < mi2:
        mi2 = a[i]

if ma1 * ma2 > mi1 * mi2:
    print(ma2, ma1)
else:
    print(mi1, mi2)
