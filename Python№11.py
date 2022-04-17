# Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system('cls')

print('Введите число N: ') 
N = int(input()) 


def get_degree(N):
    return [((-3)**i) for i in range(N)]

print (get_degree(N))