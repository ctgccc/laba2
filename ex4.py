def fun():
    while True:
        k = input("Введите целое число делитель:")
        if k.isdigit():
            f = int(k)
            try:
                b = 100 / f
                print(f"100 / {f} = {b}")
            except ZeroDivisionError:
                print("Деление на ноль!")
            finally:
                print("Блок try завершил свою работу!!!")
            break
        else:
            print('Ошибка, нужно ввести целое число. Повторите попытку ещё раз! ')


print("Добрый день, вы вошли в систему проверки деления на 0!")
print("Вам нужно ввести число для проверки!")
fun()
