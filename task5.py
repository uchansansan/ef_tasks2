while True:
    try:
        file_name = input("Введите имя файла: ")
        f = open(file_name, 'r')
        break
    except FileNotFoundError:
        print("Файл не найден.")
        continue

try:
    line_number = int(input("Введите номер строки: "))

    with open(file_name, "r") as file:
        lines = file.readlines()
        lines_cnt = len(lines)

        if line_number <= lines_cnt:
            print(lines[line_number - 1].strip())
        else:
            print("Заданный номер строки больше общего количества строк в файле.")

except FileNotFoundError:
    print("Файл не найден")
except ValueError:
    print("Некорректный номер строки. Введите целое число.")
except Exception as e:
    print("Произошла ошибка:", str(e))
