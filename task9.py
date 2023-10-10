days_in_month = {
    "январь": 31,
    "февраль": 28,
    "март": 31,
    "апрель": 30,
    "май": 31,
    "июнь": 30,
    "июль": 31,
    "август": 31,
    "сентябрь": 30,
    "октябрь": 31,
    "ноябрь": 30,
    "декабрь": 31,
}

try:
    with open('input.txt', "r") as file:
        lines = file.readlines()

    if len(lines) == 366:
        days_in_month['февраль'] = 29

    monthly_steps_sum = {month: 0 for month in days_in_month.keys()}

    for i, line in enumerate(lines):
        month, steps = line.strip().split()
        steps = int(steps)
        monthly_steps_sum[month] += steps

    with open('output.txt', "w") as file:
        for month, days in days_in_month.items():
            average_steps = monthly_steps_sum[month] / days
            file.write(f"{month}: {average_steps:.2f}\n")

except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Произошла ошибка:", str(e))
