a = [8, 4, 0, 34, 'qwerty', 'ad9']
print(a)
print(a[-1])
print(a[0:2])
print(a[:])
a[4] = 987
print(f'a[4]: {a[4]}')

elements = {
    'air' : 'воздух',
    'water' : 'вода',
    'earth' : 'земля',
}
elements['fire'] = 'огонь'
print(elements)
print(elements.values())
print(elements.keys())
len(elements)
print(len(elements))

print('elements: ', elements)
print('elements: ' + str(elements))

print('elements: {}'.format(elements))
print(f'elements: {elements}')

print(2 ** 2)
print(10 % 3) 
print(10 // 3)

print('строка 1' + ' - ' + 'строка 2')

print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 2)

print('vgfsdgf' in 'fjhgvdfjgvkdsjvgjfdvgfsdgfvkgsjkgvuyksgg')
print('vjkfsh' not in 'vd.fvvdflkjhvgfdshjvgfdsvkjdsvvvvgfhvf')

print(34 in a)
print(34 not in a)

elements_list = [1, 4, 5, 90, 8]
elements_list[0]

elements_dict = {
    0: 1,
    1: 4,
    2: 5,
    3: 90,
    4: 8
}

elements_dict[0]

print([2, 4, 7] + [1, 5])

if 'Условие 1':
    pass
elif 'Условие 2 - проверится, если первое False':
    pass
else: # Выполнится если все остальные False
    pass

i = 0

while True:
    if i > 100: break

    print(i)
    i += 1


i = 0
while i <= 100:
    print(i)
    i += 1


for element in list():
    print(i)

for i in a:
    print(i)

print('----------------------------------------------------')



# elements = {
#     'air' : 'воздух',
#     'water' : 'вода',
#     'earth' : 'земля',
# }

for element in elements:
    print(f'{element} = {elements[element]}')


for key, value in elements.items():
    print(f'{key} = {value}')



min_value = 0
not_max_value = 100
step = 1

for value in range(min_value, not_max_value, step):
    print(value)


print('----------------------------------------------------')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])

print(b)