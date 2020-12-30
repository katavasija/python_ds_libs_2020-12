# coding: utf-8
# """
# task1
# Создайте массив Numpy под названием "a" размером 5x2 (5 строк и 2 столбца). 
# Первый столбец должен содержать числа 1, 2, 3, 3, 1;
# второй - числа 6, 8, 11, 10, 7.
# Каждый столбец - это признак, а строка - наблюдение
# Найдите среднее значение по каждому признаку, 
# используя метод mean массива Numpy. 
# Результат запишите в массив mean_a (должен содержать 2 эл-та).
# """

# In[1]:
import numpy as np
# In[2]:
a = np.array([
    [1, 6],
    [2, 8],
    [3, 11],
    [3, 10],
    [1, 7]
])
# In[3]:
mean_a = a.mean(axis = 0)
mean_a
# Out[3] array([2. , 8.4])

# """
# task2
# Вычислите массив a_centered, отняв от значений массива "а" средние значения соответствующих признаков, 
# содержащиеся в массиве mean_a. 
# Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.
# """

# In[4]:
a_centered = a - mean_a
a_centered

# Out[4]
# array([[-1. , -2.4],
#       [ 0. , -0.4],
#       [ 1. ,  2.6],
#       [ 1. ,  1.6],
#       [-1. , -1.4]])
#

