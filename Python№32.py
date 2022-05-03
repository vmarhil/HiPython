# Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной 
# последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

from enum import unique
from tokenize import Number
Number=[1,5,5,5,6,6,7,7,8,9,10]
unique_numbers = list(set(Number))
print(unique_numbers, end = '')