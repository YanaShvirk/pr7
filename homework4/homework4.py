def solve_equation(a, b, c):
    return a + b * 4 - c
a = float(input("Введите значение для a: "))
b = float(input("Введите значение для b: "))
c = float(input("Введите значение для c: "))
result = solve_equation(a, b, c)
print(f"Результат уравнения x = a + b * 4 - c: {result}")
