# 6. Вводится число. Найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4)

num = int(input("Введите чётное число: "))
degree = 0

if not num % 2 and num > 0:
    while not num % 2:
        num = num // 2      # или num >> 1, но я разницу не увидел при подсчёте
        degree += 1         # или просто что-то неправильно сделал
    print("Максимальный делитель, являющийся степенью двойки:", 2 ** degree)
else:
    print("Число должно быть чётным и больше нуля")