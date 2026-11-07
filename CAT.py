def calculator():
    print("Простой калькулятор на Python")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'q'")

    while True:
        try:
            num1_str = input("\nВведите первое число: ")
            if num1_str.lower() == 'q':
                print("Выход из программы.")
                break

            num1 = float(num1_str)
            operation = input("Введите операцию (+, -, *, /): ")
            if operation.lower() == 'q':
                print("Выход из программы.")
                break

            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Ошибка: неверная операция!")
                continue

            print(f"Результат: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("Ошибка: пожалуйста, введите числовые значения.")


if __name__ == "__main__":
    calculator()
