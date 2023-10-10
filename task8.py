try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if int(line.strip()) != 100]

    with open("input.txt", "w") as file:
        file.writelines(filtered_lines)
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Произошла ошибка:", str(e))
