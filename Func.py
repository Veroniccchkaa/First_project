def FuncSum(nums: list[int]) -> int:
    """Суммирует значения списка"""

    sumNum = 0
    for num in nums:
        sumNum += num 
        
    return sumNum


def CumSum(numbers: list[int]) -> list[int]:
    """Выдает накопиптельную сумму"""
   
    for ind in range(0, len(numbers)):
        if ind != 0:
            numbers[ind] = numbers[ind] + numbers[ind - 1]
    
    return numbers


print(CumSum([1, 2, 3, 4]))
