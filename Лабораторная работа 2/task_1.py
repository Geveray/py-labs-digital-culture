money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital + salary - spend  # первый месяц
month_count = 0

while budget > 0:
    month_count += 1  # прошли проверку - прожили месяц
    spend *= 1 + increase
    budget += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
