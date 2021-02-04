def TowerOfHanoi(n, source, destination, auxiliary):  # Название функции и аргументы (столбики), n - число колец
    if n == 1:  # Если n равно 1, то
        print("peg 1 from", source, "to",
              destination)  # вывести перемещение кольца 1 со столбика source на столбик destination
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)  # Перемещение кольца, отнимается один шаг
    print("peg", n, "from", source, "to", destination)  # Выводит ход кольца n из столбика source на столбик destination
    TowerOfHanoi(n - 1, auxiliary, destination, source)  # Перемещение еще кольца, отнимается один шаг


n = int(input("Number of pegs: "))  # Ввод количества колец
TowerOfHanoi(n, 'A', 'B', 'C')  # Вызов функции
