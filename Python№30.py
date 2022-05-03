# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d≤10-10

import os
os.system('cls')
from math import *
d = 0.000001
number = 3.141545684123548993
print(number)
i = 0
def acc(d, i):
    while d < 1:
        d = d * 10
        i = i + 1
    return i
def accuracy(number):
    number = int(number * 10 ** j) / 10 ** j
    return print(number)

j = acc(d, i)
accuracy(number)

