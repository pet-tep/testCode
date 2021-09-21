file = open('file.txt')
array = file.read().split()

result = []
for i in array:
    result += [int(i)]

suma = 0
for i in result:
    suma += i

min = result[0]
for i in result:
    if i < min:
        min = i

max = 0
for i in result:
    if i > max:
        max = i

print(f'min: {min}, max: {max}')