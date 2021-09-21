file = open('file.txt')
array = file.read().split()

result = []
for i in array:
    result += [int(i)]

print(result)