
def greet(user):
    print(f'Welcome to the match app {user}!')

def challenge():
    print('1.Guess who will win the match')

def tickets():
    print('1.First class = 50000L.E\n2.Second class = 25000L.E\n3.Third class = 10000L.E\n4.Normal class = 2000L.E')


def match():
    print('1.where is the match')
    print('2.match time')
    print('3.who vs who')
    print('4who is the best player in Egypt')
    print('5who is the best player in Argantina')
    print('6.go to challenge menu')
    print('7.go to seets ticket menu')

print('----WELCOME TO THE MATCH!----')

user = input('Enter your name please: ')
while user == '':
    print('Empty name')
    user = input('Enter your name!:')

greet(user)

password = input("Enter your password: ")

while password != "1234":

    if password == "":
        print("Can't be empty!")
    else:
        print("Wrong password!")

    password = input("Enter your password again: ")

print("Correct!")

print('------------IN THE APP-------------')

match()

choose = input('choose to know!:'.capitalize())
while choose == '':
    print('cant be empty!'.capitalize())
    choose = input('choose agian:'.capitalize())

if choose == '1':
    print('The match in USA')

elif choose == '2':
    print('Match will start at 9AM')

elif choose == '3':
    print('Egypt vs Argantina')

elif choose == '4':
    print('The best player is MOHAMED SALAH')

elif choose == '5':
    print('The best player is LEONAL MESSI')

elif choose == '6':
    print('-----IN CHALLENGE GUESS-----')
    challenge()
    challenges = input('1.Argantina or 2.Egypt?:')
    while challenges == '':
        print('Empty message!')
        challenges = input('Guess agian:')
    if challenges == '1':
        print('We will see soon!')
    elif challenges == '2':
        print('We will see soon!')

elif choose == '7':
    print('-----TICKET PLACE-----')
    tickets()
    ticket_class = input('what class?:')
    while ticket_class == '':
        print('empy message!'.capitalize())
        ticket_class = input('enter the class you want agian:'.capitalize())
    if ticket_class == '1':
        print('Alr it will cost 50000L.E')
        cash = input('want to pay 1.cash or 2.visa?:')
        if cash == '1':
            print('ok')
        elif cash == '2':
            print('Payment in progress...')

    elif ticket_class == '2':
        print('Alr it will cost 25000L.E')
        cash = input('want to pay 1.cash or 2.visa?:')
        if cash == '1':
            print('ok')
        elif cash == '2':
            print('Payment in progress...')
    
    elif ticket_class == '3':
        print('Alr it will cost 10000L.E')
        cash = input('want to pay 1.cash or 2.visa?:')
        if cash == '1':
            print('ok')
        elif cash == '2':
            print('Payment in progress...')
    
    elif ticket_class == '4':
        print('Alr it will cost 5000L.E')
        cash = input('want to pay 1.cash or 2.visa?:')
        if cash == '1':
            print('ok')
        elif cash == '2':
            print('Payment in progress...')

