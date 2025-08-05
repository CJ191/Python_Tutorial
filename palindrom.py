
num=int(input('enter the number '))
y=num
rev=0

while num>0:
    x=num % 10
    rev=rev*10+x
    num//=10

# print(rev)
if y==rev:
    print('palindrom')
else:
    print('not palindrom')