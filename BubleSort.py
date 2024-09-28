
def BubbleSort(numbers: list[int]) -> list[int]:
    """Сортирует список"""

    for i in numbers:
        a = 0
        for index in range(0, len(numbers) - 1):
            num_1 = numbers[index]
            num_2 = numbers[index + 1]
            if num_1 > num_2:
                numbers[index] = num_2
                numbers[index+ 1] = num_1
                a =+ 1

        if a == 0:
            break

    return numbers

print(BubbleSort([8, 0, 2, 1, 5, 7]))