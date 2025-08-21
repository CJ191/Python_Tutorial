
# #  Dictionary
# # it is mutable data type
# # also know as maping data type
# # it define as key : value pairs
# # py dict aanu jsile object

# dict1={'name' : 'vishnu','place' : 'Calicut'}
# print(dict1)
# print(type(dict1))

# dict2={
#     'name' : 'vishnu',
#     'age' : 25,
#     'place' : 'Calicut'
# }
# print(dict2)

# # defining using constructer

# dict3=dict(name= 'vishnu',place= 'kozhikode')
# print(dict3)

# # dict4=dict(
# #     name= input('Enter your Name\t'),
# #     age=int(input('Enter your Age\t')),
# #     place=input('Enter your Place\t')
# # )
# # print(dict4)
# print(dict2['age'])
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())

# # x=input('Enter key\t')

# # if x in dict2:
# #     print('yes')
# # else:
# #     print('no')

# # single value change cheyan
# dict2={
#     'name' : 'vishnu',
#     'age' : 25,
#     'place' : 'Calicut'
# }
# print(dict2)
# dict2['age']=20
# print(dict2)

# # multiple values maattam, new itme add cheyam
# dict2.update({'email':'vishnu@gmail.com','age':24,'place':'Kozhikode'})
# print(dict2)

# dict2.pop('email')
# print(dict2)

# dict2.popitem()
# print(dict2)

# unpacking

x={'name' : 'achu','age':25,'place':'kozhikode'}

for i in x:
    print(x[i])
print('-------------')
    
for i in x.values():
    print(i)
print('-------------')

for i in x.keys():
    print(i)
print('-------------')

for i in x.items():
    print(i)
print('-------------')

for i,j in x.items():
    print(i,j)
print('-------------')

y=x.copy() #ighane cheythal original dict chages varilla
