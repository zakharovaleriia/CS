
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filename_in, filename_out) -> None:
    # Чтение данных из CSV-файла и подготовка для конвертирования в JSON
    with open(filename_in, 'r', encoding='utf-8') as first_file:
        reader = csv.DictReader(first_file, delimiter=',')
        data_to_json = [row for row in reader]

    # Конвертирование в JSON
    with open(filename_out, 'w', encoding='utf-8') as second_file:
        json.dump(data_to_json, second_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")

