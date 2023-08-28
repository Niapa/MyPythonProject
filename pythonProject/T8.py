"""Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
# в ответе получим числа x1  и x2

import math
s = int(input("Введите сумму чисел S: "))
p = float(input("Введите произведение чисел P:"))
print("Решаем уравнение вида: x^2 -s*x + p = 0")
a = 1
b = -1*s
c = p
# print("a = 1, b = " -1*s ", c = " p)
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x1 = %.2f" % x)
    print("x2 = %.2f" % x)
else:
    print("Корней нет")

