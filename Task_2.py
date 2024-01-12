"""
Користувач вводить два числа.
Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
"""
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

match (number1, number2):
    case (num1, num2) if num1 == num2:
        print("The entered numbers are equal.")
    case (num1, num2) if num1 < num2:
        print(f"The entered numbers are not equal. In ascending order: {num1}, {num2}")
    case (num1, num2):
        print(f"Введені числа не рівні. У порядку зростання: {num1}, {num2}")