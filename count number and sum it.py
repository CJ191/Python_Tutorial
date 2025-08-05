
num = int(input('Enter the Number '))

count = 0
sum = 0

while (num > 0):
    count += 1
    y = num % 10
    sum += y
    num //= 10 #num=num//10

print('count is ',count)
print('sum is ',sum)

    