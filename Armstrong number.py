
num = int(input('Enter the Number '))

temp1 = num
temp2 = num
count = 0
sum = 0

while num > 0:
    
    count += 1
    num //= 10

while temp1 > 0:

    digit = temp1 % 10
    sum += digit ** count
    temp1 //= 10

if sum == temp2:

    print(temp2,'is an Armstrong Number')

else:

    print(temp2,'is not an Armstrong Number')