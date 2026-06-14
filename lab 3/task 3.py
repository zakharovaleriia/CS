def count_letters(text):
    all_letters = [x.lower() for x in list(text) if x.isalpha() == True]
    unique_letters = list(dict.fromkeys(all_letters))

    # Подсчитываем количество букв
    quantity_dictionary = dict()
    for letter in unique_letters:
        quantity_dictionary[letter] = all_letters.count(letter)
    return quantity_dictionary


def calculate_frequency(dictionary):
    total_number_of_letters = sum(dictionary.values())
    frequency_dictionary = dict()
    for letter, quantity in dictionary.items():
        letter_frequency = quantity / total_number_of_letters
        frequency_dictionary[letter] = letter_frequency
    return frequency_dictionary

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


final_dictionary = count_letters(main_str)

for letter, frequency in calculate_frequency(final_dictionary).items():
    print(f'{letter}: {frequency:.2f}')

