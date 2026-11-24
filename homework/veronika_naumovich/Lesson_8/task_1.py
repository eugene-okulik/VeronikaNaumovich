import random

salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])

if bonus is True:
    bonus_amount = random.randint(1, 5000)
    total_salary = salary + bonus_amount
else:
    total_salary = salary
print(f"{salary}, {bonus} - '${total_salary}'")
