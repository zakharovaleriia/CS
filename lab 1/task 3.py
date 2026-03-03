list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

number_of_players=len(list_players) #общее количество игроков

# 2 равные команды = половина от общего числа игроков

first_team=list_players[:(number_of_players//2)]
second_team=list_players[(number_of_players//2):]

print(first_team)
print(second_team)

