import math

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    operation = input("Введите номер операции: ")

    if operation == '11':
        print("Конец.")
        break

    if operation in ('1', '2', '3', '4', '5'):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if operation == '1':
            result = a + b
        elif operation == '2':
            result = a - b
        elif operation == '3':
            result = a * b
        elif operation == '4':
            if b == 0:
                print("Деление на 0 невозможно.")
                continue
            result = a / b
        elif operation == '5':
            result = a ** b

    elif operation in ('6', '7', '8', '9', '10'):
        c = float(input("Введите число: "))

        if operation == '6':
            if c < 0:
                print("Квадратный корень отрицательного числа не может быть.")
                continue
            result = math.sqrt(c)
        elif operation == '7':
            if c < 0:
                print("Факториал отрицательного числа не может быть.")
                continue
            result = math.factorial(int(c))
        elif operation == '8':
            result = math.sin(c)
        elif operation == '9':
            result = math.cos(c)
        elif operation == '10':
            result = math.tan(c)

    else:
        print("Невозможный выбор операции.")
        continue

    print(f"Результат: {result}")
    