
# 1 Question

Row=int(input('Enter the no.of Rows\t'))

Start=1

for i in range(Row): #no.of rows
    for j in range(i+1): #no.of column
        print(Start,end='  ')
        Start+=1 #valuse increment cheyan
    print()