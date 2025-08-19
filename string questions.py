
# 1 question

# s1=input('first string\t')
# s2=input('second string\t')

# new_string = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
# print('new string is',new_string)


# 2 question

# s1=input('enter the string\t')

# length=len(s1)

# if length>2:
#     new_string=s1[0:2]+s1[-2:]
#     print(new_string)
# elif length==2:
#     new_string=s1[0:2]+s1[0:2]
#     print(new_string)
# elif length<2:
#     print(s1)

 
# 3 question

# x = input('Enter the String')
# upper=0
# lower=0
# digit=0
# special=0
# for i in x:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         special+=1
# print('there are',upper,'Upper Case')
# print('there are',lower,'Lower Case')
# print('there are',digit,'Digits')
# print('there are',special,'Special Characters')

# 4 question

# str=input('Enter your String\t')

# length=len(str)

# if str.endswith('ing'):
#     print(str+'ly')
# elif length>=2:
#     print(str+'ing')
# elif length<2:
#     print(str)

# 5 question

# string=input('enter your string\t')
# sub=input('enter your sub-string\t')

# index=string.index(sub)
# print(index)

# 6 Question

# string=input('Enter the String\t')
x='abcd abcd abcd abcd'

slice=x[0]+x[1:].replace(x[0],'$')
print(slice)

