# 6.  Проверить истинность высказывания: "Данное целое число является нечетным трехзначным числом".
# 19.  Даны координаты (как целые от 1 до 8) двух различных полей шахматной доски. Если слон за один ход может перейти
# с одного поля на другое, вывести логическое значение True, в противном случае вывести значение False.

def check_num_digits_value_by3(value):
    return len(str(value)) < 3 or len(str(value)) > 3


# Задание 6
# Проверка числа на кратность 3 и на 3х значность
def check_num_by3(value):
    if check_num_digits_value_by3(value):
        return False

    return value % 3 == 0


# Задание 19
# Проверка хода слона
def officer_can_go(x1, y1, x2, y2):
    if x1 < 1 or x1 > 8 or x2 < 1 or x2 > 8 or y1 < 1 or y1 > 8 or y2 < 1 or y2 > 8:
        return False
    if x1 == x2 and y1 == y2:
        return False

    return ((x1 + y1) % 2 > 0) and ((x2 + y2) % 2 > 0) or ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0)


# Задание 6

print(check_num_by3(int(input("Введите 3х значное число: "))))

# Задание 9
print(officer_can_go(int(input("Введите x1: ")), int(input("Введите y1: ")), int(input("Введите x2: ")),
                     int(input("Введите x3: "))))
