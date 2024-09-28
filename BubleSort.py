numbers = [8, 0, 2, 1, 5, 7]
# for number in numbers:
#     if number in (1, 3, 5,):
#         print('have')
#     else: 
#         print('no have')


# print(numbers[0])

# for index in range(0, len(numbers)):
#     print(numbers[index])

for i in numbers:
    a = 0
    for index in range(0, len(numbers) - 1):
        num_1 = numbers[index]
        num_2 = numbers[index + 1]
        if num_1 > num_2:
            numbers[index] = num_2
            numbers[index+ 1] = num_1
            a =+ 1
        print(numbers)
        
    if a == 0:
        break        
