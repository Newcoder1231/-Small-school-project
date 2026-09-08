def menu():
    print('1.Course name')
    print('2.Course price')
    print('3.Who is the teacher')
    print('4.I want to pay')
price = 100
username = input('Enter your name: ')
age = input('Enter your age: ')
print('Attention please -- if u are Egyption you will get 50% !dicount!')
country = input('What is your country?: ')
print('-'*30)
menu()
choose = input('choose to know!: ')
if choose == '1':
    print('Python course')
elif choose == '2':
    print('$100 without the dicount')
elif choose == '3':
    print('Ahmed foad')
elif choose == '4':
    print(f'Welcome {username}! you are from {country}! \n course price will be ',end="")
    if country  == 'Egypt':
        print(price / 2)
    else:
        print(price)