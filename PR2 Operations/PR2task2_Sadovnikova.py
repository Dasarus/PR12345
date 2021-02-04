d = int(input('Введите свой день рождения: '))
if d < 1 or d > 31:
    print("Неверный формат дня")
else:
    m = int(input('Введите свой месяц рождения: '))
    if m < 1 or m > 12:
        print("Неверный формат месяца")
    else:
        year = int(input('Введите свой год рождения: '))
        y = year % 100
        c = year // 100
        if m > 2:
            y = y
        else:
            y = y - 1
        if m > 2:
            m = m - 2
        else:
            m = m + 10
        formula = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
        numday = formula % 7
        print(numday)
