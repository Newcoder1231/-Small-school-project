
def age_sign_in():
    while True:
        try:
            age = int(input("What is your age?: "))
            while age == '':
                print("you can't let it empty!")
                age = int(input("What is your age?: "))
            if age >= 18:
                print("Sorry, we need less than 18 years old")
            else:
                print("Alright, you can continue")
            break
        except ValueError:
            print("Please enter a number")


def sign_in():
    username = input('Enter your name: ')
    while username =='':
        print("It's empty!")
        username = input('Enter your name: ')
        print(f'Welcome {username}!')
    print(f'Welcome {username}!')
    
    create_password = input('Create a password please: ')
    while create_password == '':
        print("it's empty!")
        create_password = input('Create a password please: ')
    confirm_password = input('Confirm your password: ')
    attempts = 1
    while confirm_password == '':
        print("it's empty")
        confirm_password = input('Confirm your password: ')

    while attempts <= 2:
        if confirm_password == create_password:
            print("All good")
            break
        else:
            print('False try again')

        attempts += 1
        if attempts <=2:
            confirm_password = input('Confirm your password: ')
    if attempts > 2:
        print('Bye Bye!')
           
sign_in()
