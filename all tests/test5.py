def greet(username):
    print(f'welcome,{user}!')

def menu():
    print('1.House address')
    print('2.House details')
    print('3.House price')
    print('4.Wanna call the owner?')
    print('5.Exit')

user = input('Enter your name:')
print('----WELCOME----')
greet(user)
print('----------------') 
menu()
choose = input('Choose to know:')
if choose == '1':
    print('--------------')
    print('House adress \nPortsaid\nogena we elgesh street\nyasky apartment\nfloor 8')
elif choose == '2':
    print('--------------')
    print('2 Bathroom\n1 Kitchen\n3 Rooms')
elif choose == '3':
    print('--------------')
    print('1.2M')
elif choose == '4':
    print('--------------')
    print('Phone number:01270760509')
elif choose == '4':
    print('Bye') 