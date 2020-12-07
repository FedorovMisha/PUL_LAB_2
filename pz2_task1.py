import math


# 6. Стоимость А метров серой ткани равна В рублей,
# а стоимость K метров синей ткани равна М рублей. Какая ткань дороже и на сколько?
# 66. Найти координаты точек пересечения прямой y=kx+b и окружности радиуса
# R с центром в начале координат. Определить, сколько точек пересечения находится во II координатной четверти.
# 39.	Мышонок Джерри улепетывает к своей норке по прямой.
# Успеет ли кот Том догнать Джерри, если Джерри находится как раз на полпути между Томом и норкой?

# расчет цены за единицу
def get_unit_price(price, productCount, unit):
    return (price * unit) / productCount


# Задание 6
# получить кортеж из названия и на сколько выгоден товар из двух
def get_profitable_product(costA, sizeA, costB, sizeB):
    costMeterA = get_unit_price(costA, sizeA, 1)
    costMeterB = get_unit_price(costB, sizeB, 1)
    return "Ткань A" if max(costMeterA, costMeterB) == costMeterA else "Ткань Б", max(costMeterA, costMeterB) - \
           min(costMeterA, costMeterB)


# определить четверть
def get_quarter(x, y):
    if (x > 0) and (y > 0):
        return 1
    if (x < 0) and (y > 0):
        return 2
    if (x < 0) and (y < 0):
        return 3
    if (x > 0) and (y < 0):
        return 4
    return -1


# Задание 66
# получить с количеством точек
def get_number_of_points_in_quarter(r, k, b):
    d = math.pow(2 * k * b, 2) - 4 * (1 + math.pow(k, 2)) * (math.pow(b, 2) - math.pow(r, 2))
    e = 0.000000000001
    if d < 0.0:
        return 0
    elif math.fabs(d) < e:
        x1 = (-k * b) / (1 + math.pow(k, 2))
        y1 = k * x1 + b
        quarter = get_quarter(x1, y1)
        if quarter == 2:
            return 1
    else:
        x1 = (-2 * k * b - math.sqrt(d) / (2 * (1 + math.pow(k, 2))))
        x2 = (-2 * k * b + math.sqrt(d) / (2 * (1 + math.pow(k, 2))))
        y1, y2 = k * x1 + b, k * x2 + b
        quarter1 = get_quarter(x1, y1)
        quarter2 = get_quarter(x2, y2)
        res = int(quarter1 == 2) + int(quarter2 == 2)
        return res

    return 0


# Задание 39
# Сможет ли 1 догнать 2 если известна их скорость и их расстояние
def can_catchup(speed1, speed2, size1, size2):
    time1 = size1 / speed1
    time2 = size2 / speed2
    return time1 <= time2


# Задание 66 Выполнение

R, K, B = float(input("Введите радиус: ")), \
          float(input("Введите k: ")), \
          float(input("Введите b: "))
print("\nКол-во точек пересечения находящихся в II координатной четверти: ",
      int(get_number_of_points_in_quarter(R, K, B)), "\n")

# Задание 6 Выполнение
SizeA = float(input("Введите размер в метраз Ткани A: "))
CostA = float(input("Введите стоимость Ткани А за " + str(SizeA) + "метров: "))
SizeB = float(input("Введите размер в метраз Ткани B: "))
CostB = float(input("Введите стоимость Ткани А за " + str(SizeB) + "метров: "))
result = get_profitable_product(costA=CostA, costB=CostB, sizeA=SizeA, sizeB=SizeB)
print("\n Самая дорогая ткань: ", result[0], "\t: Она дороже на ", result[1], "\n")

# Задание 39 Выполнение

Distance = float(input("Введите дистанцию до норки: "))
SpeedTom = float(input("Введите скорость Тома: "))
SpeedJerri = float(input("Введите скорость Джерри: "))

print("Том еспеет догнать Джерри" if can_catchup(SpeedTom, SpeedJerri, Distance, Distance / 2.0)
      else "Том не успеет догнать джерри")
