import sys

from p.find_way import find_way
from p.get_way import get_way
from p.display_way import display_way


def main():
    """
    Главная функция программы.
    """
    # Маршруты
    ways = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о маршруте.
            way = get_way()

            # Добавить словарь в список.
            ways.append(way)
            # Отсортировать список в случае необходимости.
            if len(ways) > 1:
                ways.sort(key=lambda item: item.get('num', 0))

        elif command == 'list':
            # Отобразить все маршруты.
            display_way(ways)

        elif command == 'find':
            f = input('Введите номер маршрута: ')
            selected = find_way(ways, f)
            display_way(selected)

        elif command == 'help':
            # Вывести справку.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("find - вывод информации о маршруте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
