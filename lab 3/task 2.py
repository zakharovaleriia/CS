def find_common_participants(first_string, second_string, split_sign = ','):
    # Конвертация строки в множество через разделитель
    first_iterable = set(first_string.split(split_sign))
    second_iterable = set(second_string.split(split_sign))

    # Поиск пересечения множеств = общих участников
    common_part = first_iterable.intersection(second_iterable)
    return list(sorted(common_part))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, split_sign = '|'))
