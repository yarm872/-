#Напишите программу, которая вводит два целых числа, a и b ( a < b ),
#и выводит через пробел 5 случайных целых чисел на отрезке [ a , b ] .
#
from random import randint
a,b=map(int,input().split())
print(randint(a,b),randint(a,b),randint(a,b),randint(a,b),randint(a,b))
