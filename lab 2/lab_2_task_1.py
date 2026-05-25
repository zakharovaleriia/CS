money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Итоговое кол-во месяцев
months = 0

for month in range(1000):

    loan = spend - salary
    spend *= (1 + increase)  # Увеличение расходов из-за повышения цен

    if money_capital > loan:  # Проверка возможности использования подущки без.
        money_capital -= loan
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)


