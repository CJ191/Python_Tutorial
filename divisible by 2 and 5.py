x=int(input('Enter a Number '))

# if (x % 2 == 0 and x % 5 == 0):
#     print('The given Number is Divisible By 2 and 5')
# else:
#     print('The given Number is not Divisible By 2 and 5')


if (x % 2 == 0):
    if (x % 5 == 0):
        print(x,'Divisible by 2 and 5')
    else:
        print(x,'divisible by 2, not 5')
else:
    if (x % 5 == 0):
        print(x,'divisible by 5, not 2')
    else:
        print(x,'not divisible by both')
            