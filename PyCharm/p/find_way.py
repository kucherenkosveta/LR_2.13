def find_way(numbers, nw):
    """
    Выбрать маршрут с данным номером.
    """
    # Список маршрутов
    result = []
    for h in numbers:
        if nw in str(h.values()):
            result.append(h)

    # Проверка на наличие записей
    if len(result) == 0:
        return None

    # Возвратить список выбранных маршрутов.
    return result
