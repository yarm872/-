'''Напишите программу, которая считает сумму цифр введённого числа.

Входные данные
Входная строка содержит одно натуральное число.

Выходные данные
Программа должна вывести сумму цифр введённого числа.'''
import sys
sys.setrecursionlimit(20000)
n=int(input())
def f(n,k):
    if n==0:
        return k
    k+=(n%10)
    return f(n//10,k)
k=0
if n==0:
    print(0)
elif n<0:
    n=-n
    print('-',end='')
    print(f(n,k))
else:
    print(f(n,k))