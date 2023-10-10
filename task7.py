try:
    with open("input.txt", "r") as input_file:
        numbers = input_file.readlines()

    result = int(numbers[0]) / int(numbers[1]) + int(numbers[2])

    with open("output.txt", "w") as output_file:
        output_file.write(str(result))

except FileNotFoundError:
    print("Файл не найден")
except ValueError:
    print("Некорректный формат чисел в файле")
except ZeroDivisionError:
    print("Деление на ноль")
except Exception as e:
    print("Произошла ошибка:", str(e))
