# Tuple
# immuttable data type
# constrocter tuple

x=('a',1,True)
print(x)
print(type(x))
print(len(x))
print(x[2])
print(x[-2])

x=(1,2,3,10,4,5)
print(sum(x))
print(min(x))
print(max(x))
print(x[:4])
print(x[1:])
print(x[-4:-2])

x=('a','b','c','d','e')

if 'b' in x:
    print('yes')

for i in x:
    print(i)

x=('b',) #single element tuple create aakan element kazhinj , idannam alenkil ath string or int aayitt return cheyya
