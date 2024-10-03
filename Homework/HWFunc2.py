def SumLists(list_one: list, list_two: list) -> list:
    """
        Суммирует 2 спискаоз
        Возвращает третий список с элементами обеих

    """

    list_three = []
    for char in list_one:
        if char in list_three:
            pass
        else:
            list_three.append(char)
   
    for char in list_two:
        if char in list_three:
            pass
        else:
            list_three.append(char)

    return list_three

print(SumLists([1, 3, 5, 7], [1, 6, 9]))
    