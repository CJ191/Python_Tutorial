
# 1 question

# s1=input('first string\t')
# s2=input('second string\t')

# new_string = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
# print('new string is',new_string)


# 2 question

s1=input('enter the string\t')

length=len(s1)

if length>2:
    new_string=s1[0:2]+s1[-2:]
    print(new_string)
elif length==2:
    new_string=s1[0:2]+s1[0:2]
    print(new_string)
elif length<2:
    print(s1)

 
