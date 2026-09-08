school_name = 'asfory school'
owner_name = 'ahmed fo2aad'

def greet(name):
    print(f'welcome to our school page {name}!')
print('----------------------------')

def menu():
    print('1.say hi'.capitalize())
    print('2.say bye'.capitalize())
    print('3.owner name'.capitalize())
    print('4.school name'.capitalize())
    print('5.school details'.capitalize())

name = str(input('enter your name: '.capitalize()))
while name == '':
    print('your name is empty '.capitalize())
    name = input('enter your name agian: '.capitalize())

while True:

    menu()
    choice = input('choose: '.capitalize())
    while choice == '':
        print('empty agian?'.capitalize())
        choice = input('choose agian:'.capitalize())

    if choice == '1':
        print(f'Hi {name}!')

    elif choice == '2':
        print(f'Bye bye {name}!')

    elif choice == '3':
        print(f'Owner name is {owner_name}!')

    elif choice == '4':
        print(f'School name is {school_name}!')

    elif choice == '5':
        print('6 months = 6000L.E \n 1 year =12000L.E')

    break



          