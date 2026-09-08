import os
os.system('clear')
people = {
    'manager':'ahmed',
    'owner':'mahmoud',
    'workers':['gamal','saad','ghonem','foad'],
    'worker_job =':{
        'gamal':'cashier',
        'saad':'cashier',
        'ghonem':'chef',
        'foad':'waiter'
    }
}

food = {
    '1' : 'meat with molokhiya - 220LE',
    '2' : 'beakata - 200LE',
    '3' : 'hawashi - 70LE',
    '4' : 'soup - 32LE'
}
def greet(username):
    print(f'Hi there {username}!')

def app_menu():
    print('1.the owner')
    print('2.the manager')
    print('3.workers')
    print('4.food menu')
    print('5.restaurant review')
    print('6.what time we open and address')
    print('7..exit')

def restaurant_address():
    print('PORTSAID\nAhmed oraby STREET\nnext to molarad hospital')

def time():
    print('9AM TO 12PM')

print('-----RESTAUTANT APP-----')

username = input('Enter your name:')
while username == '':
    print("can't be empty".upper())
    username = input('Enter your name:')

password = input('Password:')
while password == '':
    print("can't be empty".upper())
    password = input('Password:')

confirm = input("Confirm password:")
while confirm == '':
    print("can't be empty".upper())
    confirm = input('Confirm password:')
while confirm != password:
    print('uncorrect!'.upper())
    confirm = input('confirm password:')

greet(username)

print('--------')

app_menu()
choose = input('choose:'.capitalize())
if choose == '1':
    print(f'the manager is {people['manager']}'.capitalize())

elif choose == '2':
    print(f'the owner is {people["owner"]}'.capitalize())
elif choose =='3':
    print('----------------------')
    choose_work = input('1.workers job\n2.workers names\nchoose:')
    while choose_work == '':
        print('just type 1/2'.capitalize())
        choose_work = input('1.workers job:\n2.workers names:')
    if choose_work == '1':
        print('-----------')
        for worker1 in people['workers']:
            print(f'{worker1} : {people["worker_job ="][worker1]}')

    elif choose_work == '2':
        print('-----------')
        for worker2 in people['workers']:
            print(worker2)

elif choose =='4':
    for number,item in food.items():
        print(f'{number}. {item} ')
    choice = input('need somthing?'.capitalize())
    while choice == '':
        print('empty!'.upper())
        choice = input('need somthing?')
    if choice == '1':
        payment = input('1.cash/.2visa')
        if payment == '1':
            print('ok')
        elif payment == '2':
            print("ok")
    elif choice == '2':
        payment = input('1.cash/.2visa')
        if payment == '1':
            print('ok')
        elif payment == '2':
            print("ok")
        
    elif choice == '3':
        payment = input('1.cash/.2visa')
        if payment == '1':
            print('ok')
        elif payment == '2':
            print("ok")
        
    elif choice == '4':
        payment = input('1.cash/.2visa')
        if payment == '1':
            print('ok')
        elif payment == '2':
            print("ok")   
        
elif choose == '5':
    rate = input('rate us 1 to 10:')
    while rate == '':
        print('empty!'.upper())
        rate = input('rate us 1 to 10:')
    if rate <= '7':
        print('we are so sorry'.capitalize())
    else:
        print('thank you!'.upper())

elif choose == '6':
    print('----ADDRESS----')
    restaurant_address(),print(end=' ')
    print('----TIME----')
    time()

elif choose == '7':
    print(f'bye {username}!'.upper())