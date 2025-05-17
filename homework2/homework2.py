
def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]
decimal_number = int(input("Введите десятичное число: "))

binary = decimal_to_binary(decimal_number)
octal = decimal_to_octal(decimal_number)
print(f"Двоичное представление: {binary}")
print(f"Восьмеричное представление: {octal}")
