#исходные данные

card_storage=1.44 #объем дискеты в Мб
card_storage_bites=1.44*1024*1024 #объем дискеты в байтах
pages_per_book=100 #количество страниц в одной книге
strings_per_page=50 #количество строк на одной странице
symbols_per_string=25 #количество символов на одной строке
bites_per_symbol=4 #количество байт, занимаемых одним символом

string_storage=bites_per_symbol*symbols_per_string #объём, занимаемый одной строкой

page_storage=strings_per_page*string_storage #объём, занимаемый одной страницей

book_storage=pages_per_book*page_storage #объём, занимаемый одной книгой

books_per_card=int(card_storage_bites//book_storage) #количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_per_card)

