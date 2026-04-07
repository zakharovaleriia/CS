import json

JSON_FILENAME = 'input.json'


def task(filename) -> float:
    # Чтение данных из JSON-файла
    with open(filename) as file:
        data = json.load(file)

    # Обработка данных
    sum_of_products = sum(value['score'] * value['weight'] for value in data)
    return round(sum_of_products, 3)


print(task(JSON_FILENAME))
