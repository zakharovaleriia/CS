def finding_first_item(iterable, specific_item):
    # Проверка наличия нужного товара в списке
    if len([x == specific_item for x in iterable]) > 0:

        # Поиск первого вхождения
        for item in iterable:
            if item == specific_item:
                return iterable.index(item)
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finding_first_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
