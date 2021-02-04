# Методы типа "списки":
X = [1, 2, 3, 4]
K = [5, 6]
# 1. Добавляем элемент в конец списка
X.append(16)
print(X)
# 2. Удаляем первый элемент "16" в списке
X.remove(16)
print(X)
# 3. Добавляем все элементы другого списка в конец нашего списка
X.extend(K)
print(X)
# 4. Вставляем на i-ый (в нашем случае 2) элемент значение x (в нашем случае 7)
X.insert(2, 7)
print(X)
# 5. Удаляем i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
X.pop(4)
print(X)
# 6. Разворачиваем список
X.reverse()
print(X)
# 7. Очищаем список
X.clear()
print(X)
