
limit=int(input('Enter your Limit : '))

for i in range(1,limit+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)