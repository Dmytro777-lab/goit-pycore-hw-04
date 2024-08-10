def get_cats_info(path):
    cats_info_list = []

    try: 
        with open(path, 'r') as file: # Відкриваємо файл для читання
            for line in file:
                parts = line.strip().split(',') # Видаляємо прогалини на початку і в кінці рядка і ділимо рядок по комі
                if len(parts) == 3: # Перевіряємо, чи є достатня кількість елементів у рядку
                    cats_info_list.append({
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    })
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")

    return cats_info_list


path = "cats_file.txt"
cats_info = get_cats_info(path)
print(cats_info)
