
string=input('enter something ')
length=len(string)
index=length-1

rev=''

while index>=0:
    rev=rev+string[index]
    index=index-1
if rev==string:
    print(string,'is Palindrom')
else:
    print(string,'is not a Palindrom')