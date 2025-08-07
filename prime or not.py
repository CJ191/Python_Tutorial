
num=int(input('Enter a Number '))
x=num
i=2

while (i<num):
    
    if (num%i==0):
        print(x,'Not a Prime Number')
        break
    i+=1
else:
    print(x,'is a prime number')