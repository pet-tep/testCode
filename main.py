file = open('file.txt')
array = file.read().split()

result = []
for i in array:
    result += [int(i)]

suma = 0
for i in result:
    suma += i

print(suma)