import sys
from pathlib import Path
from colorama import Fore, init
# Ініціалізуємо colorama для автоматичного скидання кольорів
init(autoreset=True)

def print_structure(path):
    for item in path.iterdir():# Виводимо імена директорій у синьому кольорі, файли у зеленому
        print(f'{Fore.BLUE if item.is_dir() else Fore.GREEN}{item.name}')
        if item.is_dir():# Рекурсивно обробляємо піддиректорії
            print_structure(item)

def main():# Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print("Usage: python hw03.py /path/to/directory")
        return
    
    directory_path = Path(sys.argv[1])# Створюємо об'єкт Path з аргументу

    if directory_path.is_dir():# Перевірка, що це директорія
        print_structure(directory_path)
    else:
        print("The specified path does not exist or is not a directory.")

if __name__ == "__main__":
    main()

