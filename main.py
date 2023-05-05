"""
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного
вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного
подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.

7.	F(x<2) = -23; F(n) = 5F(n-1) + F(n-5)

"""
import sys
import time
import matplotlib.pyplot as plt
import pylab

sys.setrecursionlimit(100000)

# -------------------------Ввод-------------------------

n = input('Введите натуральное число: ')

try:
    n = int(n)
except ValueError:
    sys.exit('Введено не натуральное число, или не число вовсе. Программа завершена.')

if n < 0:
    sys.exit('Введено не натуральное число. Программа завершена.')


# -----------------------Рекурсия------------------------

def f(number):
    # return 1
    if number < 2:
        return -23
    else:
        return int(5 * f(number - 1) + f(number - 5))


# ------------------------Итерация------------------------

def iteration(number):
    calc_list = [-23] * 6
    for j in range(2, number + 1):
        calc_list[5] = 5 * calc_list[4] + calc_list[0]
        calc_list[:4], calc_list[4] = calc_list[1:5], calc_list[5]
    return calc_list[5]


# ---------------------------------------------------------
recursion_time = []
iteration_time = []
num_list = []

for i in range(1, n + 1, 1):
    num_list.append(i)
    start_time = time.time()
    print(str(i) + ') \nРекурсия: ' + str(f(i)))

    temp = time.time() - start_time
    recursion_time.append(temp)
    start_time = time.time()
    print('Время: ' + str(temp))
    print('Итерация: ' + str(iteration(i)))

    temp = time.time() - start_time
    print('Время: ' + str(temp))
    iteration_time.append(temp)

answer = [recursion_time]
plt.plot(num_list, recursion_time, label='Рекурсия'), plt.plot(num_list, iteration_time, label='Итерация')
plt.title("График производительности"), plt.xlabel("Проверяемое число"), plt.ylabel("Время вычислений в секундах")
plt.legend()
plt.show()
