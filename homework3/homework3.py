# вариант 3:пятеричная
def decimal_to_quinary(n):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        result = str(n % 5) + result
        n //= 5
    return result


decimal_number = int(input("Введите десятичное число: "))

quinary = decimal_to_quinary(decimal_number)


print(f"Пятеричное представление: {quinary}")

