
x= dict(name=input('Enter Your Name\t'),email=input('Enter Your Email\t'),phone=[input('First Phone Number\t'),input('Second Phone Number\t')])
# x = dict(name='vishnu', email='vishnu@gmail.com', phone=[9645147354, 9961320975])

a = '1- View'
a1 = '1- Name'
a2 = '2- Email'
a3 = '3- Phone No'
a4 = '4- View All'
a31 = '1- All'
a32 = '2- First Phone No'
a33 = '3- Second Phone No'

b = '2- Add'
b1 = '1- Add Place'
b2 = '2- Add Education'

c = '3- Update'
c1 = '1- Update Name'
c2 = '2- Update Email'
c3 = '3- Update Phone No'
c31 = '1- Update First Phone No'
c32 = '2- Update Second Phone No'

d = '4- Delete'
d1 = '1- Delete All'
d2 = '2- Delete Name'
d3 = '3- Delete Email'
d4 = '4- Delete Phone No'
d41 = '1- Delete First Phone No'
d42 = '2- Delete Second Phone No'
d43 = '3- Delete All Phone No'

e = '0- Exit'

while True:
    print(
        '\nChoose Your Options\n',
        a, '\n',
        b, '\n',
        c, '\n',
        d, '\n',
        e, '\n'
    )

    choices = input('Enter your choice (0-4): ')

    if choices == '1':  # View Content
        print('You selected: View\nChoose your Option\n', a1, '\n', a2, '\n', a3, '\n', a4, '\n', '0- Go Back\n')

        viewchoice = input('Enter your choice (0-4): ')

        if viewchoice == '1':
            print('You Selected Name: ', x['name'])

        elif viewchoice == '2':
            print('You Selected Email: ', x['email'])

        elif viewchoice == '3':
            print('You selected Phone:\nChoose Your Option\n', a31, '\n', a32, '\n', a33, '\n', '0- Go Back\n')

            viewchoicephone = input('Enter your choice (0-3): ')

            if viewchoicephone == '1':
                print('You selected All: ', x['phone'])

            elif viewchoicephone == '2':
                print('You selected First No: ', x['phone'][0])

            elif viewchoicephone == '3':
                print('You selected Second No: ', x['phone'][1])

            elif viewchoicephone == '0':
                continue  

            else:
                print("Invalid choice! Please select between 0-3.")

        elif viewchoice == '4':
            print('You Selected View All: ', x)

        elif viewchoice == '0':
            continue  

        else:
            print("Invalid choice! Please select between 0-4.")

    elif choices == '2':  # Add Content
        print('You selected: Add\n','Choose your Option\n', b1, '\n', b2, '\n', '0- Go Back\n')

        addchoice = input('Enter your choice (0-2): ')

        if addchoice == '1':
            x.update({'place': input('Enter Your Place\t')})
            print('Place Added: ', x['place'])

        elif addchoice == '2':
            x.update({'education': input('Enter Your Education\t')})
            print('Education Added: ', x['education'])

        elif addchoice == '0':
            continue  

        else:
            print("Invalid choice! Please select between 0-2.")

    elif choices == '3':    # Update Content
        print('You selected: Update\n','Choose your Option\n', c1, '\n', c2, '\n', c3, '\n', '0- Go Back\n')

        updatechoice = input('Enter your choice (0-3): ')

        if updatechoice == '1':
            x.update({'name' : input('Enter the Name to Update')})
            print('Name updated to :',x['name'])

        elif updatechoice == '2':
            x.update({'email' : input('Enter the Email to Update')})
            print('Update Enail :',x['email'])

        elif updatechoice == '3':
            print('You Selected to Update Phone No\n','choose your option\n', c31,'\n',c32,'\n','0- Go Back\n')

            phoneupdatechoice = input('Enter your choice (0-2): ')

            if phoneupdatechoice == '1':
                x['phone'][0] = input('Enter the First No to Update: ')
                print('Updated First No :',x['phone'][0])

            elif phoneupdatechoice == '2':
                x['phone'][1] = input('Enter the Second No to Update: ')
                print('Updated Second No :',x['phone'][1])

            elif phoneupdatechoice == '0':
                continue  

            else:
                print("Invalid choice! Please select between 0-2.")

        elif updatechoice == '0':
            continue  

        else:
            print("Invalid choice! Please select between 0-3.")

    elif choices == '4':    # Delete Content
        print('You selected: Delete\n', 'Choose your Option\n',d1,'\n',d2,'\n',d3,'\n',d4,'\n','0- Go Back\n')

        deletechoice = input('Enter your choice (0-4): ')

        if deletechoice == '1':
            x.clear()
            print('All Files Deleted',x)

        elif deletechoice == '2':
            x.pop('name')
            print('Name Deleted',x)

        elif deletechoice == '3':
            x.pop('email')
            print('Email Deleted',x)

        elif deletechoice == '4':
            print('You Selected to Delete Phone No\n','Choose your Option\n', d41, '\n', d42, '\n', d43, '\n', '0- Go Back\n')

            phonedeletechoice = input('Enter Your Choice (0-3): ')
            
            if phonedeletechoice == '1':
                x['phone'].pop(0)
                print('First Phone No Deleted',x)

            elif phonedeletechoice == '2':
                x['phone'].pop(1)
                print('Second Phone No Deleted',x)

            elif phonedeletechoice == '3':
                x.pop('phone')
                print('All Phone No Deleted',x)

            elif phonedeletechoice == '0':
                continue  

            else:
                print("Invalid choice! Please select between 0-2.")

        elif deletechoice == '0':
            continue  

        else:
            print("Invalid choice! Please select between 0-2.")

    elif choices == '0':
        continue

    else:
        print("Invalid choice! Please select between 0-4.")
