numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_of_skipped_item=numbers.index(None) #индекс пропущенного элемента

numbers_copy=numbers.copy() #копия списка для подсчета суммы
numbers_copy.pop(index_of_skipped_item) #список без пропущенного элемента

average=sum(numbers_copy)/len(numbers) #среднее арифметическое

numbers[index_of_skipped_item]=average #замена пропущенного элемента на ср. арифм.

print("Измененный список:", numbers)