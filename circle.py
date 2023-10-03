import math

'''
Принимает значение r, возращает значение площади круга
    Параметры:
            r (int): десятичное число
    Пример:
            Получает: r=10
            Возвращает: 314
'''
def area(r):
    return math.pi * r * r


'''
Принимает значение r, возращает значение длины окружности круга
    Параметры:
            r (int): десятичное число
    Пример:
            получает: r=10
             
            возвращает: 62,8
'''
def perimeter(r):
    return 2 * math.pi * r

