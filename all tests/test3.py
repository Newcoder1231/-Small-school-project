school_name = 'Asfory school'
school_manager = 'Amgad hosney'
school_owner = 'Mohamed ramadan'
teachers_list = ['Ala ngm','Radwa','Samer','Hazem','Mohammed']

def greet(username):
    print(f'Hi there {username}!')
    print('---------------------------')

def old():
    age = (input(f'your age:'.capitalize()))
    while age == '':
        print('empty!'.upper())
        age = (input(f'your age:'.capitalize()))
    age = int(age)
    if age <= 12:
        print('sorry we need older than 12 years old'.upper())
        return False
    else:
        return True

def login_agian():
    paswd = input('Enter your password:') 
    while paswd == '':
        print('Empty!')
        paswd = input('enter your password agian:'.upper())
    if paswd == password:
        print('good'.upper())
    else:
        print('false'.upper())
    
def settings():
    print('1.change username')
    print('2.change password')
    print('3.account details')

def menu():
    print('1.say hi'.capitalize())
    print('2.say bye'.capitalize())
    print('3.who is the owner?'.capitalize())
    print('4.who is the manager?'.capitalize())
    print('5.teachers'.capitalize())
    print('6.payment details'.capitalize())
    print('7.apartment details')
    print('8.settings'.capitalize())

if old() == False:
    quit()

username = input('username:'.capitalize())
while username =="":
    print('cant be empty')
    username = input('username:'.upper())

password = input('password:'.capitalize())
while password =="":
    print('cant be empty')
    password = input('password:'.upper())

confirm = input('confirm password:'.capitalize())
while confirm =="":
    print('cant be empty')
    confirm = input('confirm:'.upper())

print('-----MENU-----')

menu()
choose = input('choose:'.capitalize())
while choose == '':
    print('cant be empty'.upper())
    choose = input('choose agian:'.upper())

if choose == '1':
    print(f'Hi {username}!')

elif choose == '2':
    print(f'Bye {username}!')

elif choose == '3':
    print(f'The owner is {school_owner}!')

elif choose == '4':
    print(f'The manager is {school_manager}!')

elif choose == '5':
    print(f'Here you go!\n {teachers_list}')

elif choose == '6':
    print('1 year = 20000L.E\n6 months = 10000L.E'.upper())

elif choose == '7':
    print('port said\nstreet:mohamed ali\nasfory school'.upper())

elif choose == '8':
    login_agian()
    print('-----SETTINGS-----')
    settings()
    setting = input('choose:'.upper())
    while setting == '':
        print('empty!'.upper())
        setting = input('choose agian'.upper())
    else:
        print('somthing is wrong!'.upper())
        setting = input('choose agian:'.upper())
    if setting == '1':
        username_change = input('write username to change:'.capitalize())
        while username_change == '':
            print('empty message'.upper())
            username_change = input('write username to change:'.upper())
        username = username_change
    elif setting == '2':
        password_change = input('write password to change:'.capitalize())
        while password_change == '':
            print('empty message'.upper())
            username_change = input('write password to change:'.upper())
        password = password_change
    elif setting == '3':
        print(f'account name is --{username}--'.capitalize())
        print(f'account username is --{password}--'.capitalize())
       
