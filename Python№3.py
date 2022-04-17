# Вывести на экран числа от -N до N
import os
os.system('cls')

a = abs(int(input('Введите число: ')))

for i in range(-a, a):
    print(i, end=' ')
