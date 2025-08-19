
# list comprehension

# syntax shorter aakan vendi
# single line code cheyan

l=['vishnu','cj','achu','arun','appu']

new=[i for i in l if 'a' in i]
# print(new)
# op ['achu', 'arun', 'appu']

new=['haii' for i in l if 'h' in i]
# print(new)
# op ['haii', 'haii']

matrix=[1,2],[3,4]

for i in range(2):
    for j in range(2):
        print(matrix[i][j],end=' ')
    # print() to goto next line
# op 1 2
  #  3 4