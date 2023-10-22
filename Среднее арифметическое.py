'''Найти среднее арифметическое целых чисел, записанных в файле input.txt в столбик. Количество чисел неизвестно. Результат записать в файл output.txt .

Входные данные
Целые числа записаны в файле input.txt в столбик, по одному в строке. Ввод заканчивается тогда, когда заканчиваются данные в файле.

Выходные данные
Программа должна вывести в файл output.txt среднее арифметическое всех чисел в файле.'''
fin=open('input.txt')
fout=open('output.txt','w')
a=[]
while True:
      s=fin.readline()
      if not s:
            break
      s=int(s)
      a.append(s)
k=0
for i in range(len(a)):
      k+=a[i]
print(k/len(a),file=fout)
fin.close()
fout.close()