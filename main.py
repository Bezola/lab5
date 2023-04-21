'''
Вариант 7.
1 часть – написать программу в соответствии со своим вариантом задания.
Задание 1: Вывести все натуральные числа до n, в записи которых встречается ровно одна нечетная цифра.
-------------------------------------------------------------------------------------------------------
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на
характеристики объектов и целевую функцию для оптимизации решения.
Задание 2: [Задание 1] + сумма цифр должна быть двузначной иметь ровно одну четную цифру в записи.
'''

import sys
control = False

odd_num_list = ['1', '3', '5', '7', '9']
#------Функция проверки чисел на четность------
def odd_check(i_num):
    odd_count = 0
    for check_num in odd_num_list:
        odd_count += str(i_num).count(check_num)
    if odd_count == 1:
        return True
    else:
        return False
#---------Функция-проверки-цифр-числа----------
def two_digit_check(num):
    check = 0
    for cypher in str(num):
        check += int(cypher)
    if len(str(check)) == 2:
        if odd_check(check):
            return True
        else:
            return False
    else:
        return False
#-------------------Задача---------------------
def default(stop_num):
    for i_num in range(1, stop_num):
        if odd_check(i_num):
            print(i_num, end=' ')
    print()

def final(stop_num):
    for i_num in range(1, stop_num):
        if odd_check(i_num):
            if two_digit_check(i_num):
                global control
                control = True
                print(i_num, end=' ')

#----------------------Ввод--------------------
try:
    stop_num = int(input('Введите число n > 1 до которого будут совершены расчёты: '))
    if stop_num < 2:
        sys.exit('Число должно быть больше 1. Программа завершена.')
except ValueError:
    sys.exit('Введено не число. Программа завершена.')

#---------------------Вывод--------------------
print('Часть 1:')
default(stop_num)

print('Часть 2:')
final(stop_num)
if not control:
    print('Подходящих чисел нет')
