x=int(input('Enter the Unit '))

if (x <= 100):
    print(x,'units, no charges for This unit')
elif (x > 100 and x <= 200):
    i = (x-100)*5
    print(x,'units you have to pay',i)
elif (x > 200):
    i = (x-200)*10
    print(x,'units you have to pay',i+500)

