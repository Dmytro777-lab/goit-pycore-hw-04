def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                # Видаляємо прогалини на початку і в кінці рядка і ділимо рядок по комі
                name, salary = line.strip().split(',')
                # Перетворимо зарплату на ціле число і додаємо до загальної суми
                total += int(salary)
                count += 1

        if count == 0:
            return 0

        # Повертаємо загальну та середню зарплату
        return total, total / count

    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return 0

path = 'salaries.txt'
total, average = total_salary(path)
print(f"Общая сумма зарплат: {total}")
print(f"Средняя зарплата: {average}")

