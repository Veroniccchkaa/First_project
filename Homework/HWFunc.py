def Factorial(number: int) -> int:
    """Считает факториал числа"""

    fact = 1
    for num in range(2, number + 1):
        fact *= num

    return fact
print(Factorial(5))


