def is_valid_year(year):
    try:
        year = int(year)
        if year < 0:
            return False
        return True
    except ValueError:
        return False


def chinese_zodiac(year):
    zodiac_animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Кролик", "Дракон", "Змея",
                      "Лошадь", "Овца"]
    zodiac_index = (year-4)% 12
    return zodiac_animals[zodiac_index]


while True:
    user_input = input("Введите год (0 для выхода): ")

    if user_input == "0":
        break

    if not is_valid_year(user_input):
        print("Некорректный год. Попробуйте снова.")
        continue

    year = int(user_input)
    zodiac = chinese_zodiac(year)
    print(f"Год {year} по китайскому календарю: {zodiac}")
