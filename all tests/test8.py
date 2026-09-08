school_manager = 'Amgad Hosney'
def exit_or():
    choose_exit = input('Want to| 1.menu or 2.quit')
    if choose_exit == '1':
        menu()
    elif choose_exit == '2':
        exit()
def settings():
    print('1.Change password')
    print('2.Change username')
    print('3.Change age')

def menu():
    school_menu = ('1.School manager\n'
    '2.School address\n'
    '3.School details\n'
    '4.Payment details\n'
    '5.Account settings\n'
)
    return school_menu

def user_account(username,login_age,country,password):
    account = {'Name':username,
               'Your age is':login_age,
               'Your country is':country,
               'Your password is':password
}
    return account
#
#
name = input('Enter your name: ')   #in def
while name == '':
    print('Its empty!')
    name = input('Enter your name: ')

name_confirm = input('Confirm your name: ')     #No
if name_confirm != name:
    print('Try agian')
    name_confirm = input('Confirm your name agian: ')
    if name_confirm != name:
         exit()
    else:
        print('True')
#
#
user_check = input('Are you a | 1.parent or 2.student?')
if user_check == '1':
    parent_login_age = int(input('Enter student age: '))               #in def
    while parent_login_age == '':
        print('Its empty!')
        parent_login_age = int(input('Enter student age agian: '))

    if parent_login_age >18:
        print(f'Sorry school for under 17 years old')
        exit()
    else:
        pass

elif user_check == '2':
    student_login_age = int(input('Enter your age: '))
    if student_login_age > 18:
        print('Sorry school for under 17 years old')
        exit()
    else:
        pass
#
#
country = input('Enter your country: ')             #in def
#
#
create_password = (input('create your password:'))
while create_password == '':
    print('Its empty!')
    create_password = (input('create your password: '))

confirm_password = (input('Confirm your password: '))
while confirm_password == '':
    print('Its empty!')
    confirm_password = (input('Confirm your password: '))
    if confirm_password != create_password:
        print('Try agian')
        confirm_password = (input('Confirm your password: '))
    else:
        pass
#
#
while True:
    print('-'*30)
    print(f'weclome to school app!')
    print(menu())
    choose = input('Choose to know: ')
    if choose == '1':
        print(f'School manager is {school_manager}!')
        exit_or()
    elif choose == '2':
        print('port said\nstreet:mohamed ali\nasfory school')
        exit_or()
    elif choose == '3':
      
         print('1 year = 20000L.E\n6 months = 10000L.E')
         exit_or()
    elif choose == '4':
        print('You can pay a depposit to VODAFONE CASH \n 012776161183')
        exit_or()
    elif choose == '5':
        settings()
        print('Your account information')
        if user_check == '1':
            login_age = parent_login_age
        elif user_check == '2':
            login_age = student_login_age

        account_info = user_account(
            username=name,
            country=country,
            login_age=login_age,
            password=create_password
)
        print('This is your information')
        print(account_info)
        print('-'*30)
        settings()
        choose_settings = input('choose to know: ')
        if choose_settings == '1':
            passwd_change = input('Write the new password:')
            while passwd_change == '':
                print('Its empty!')
                passwd_change = input('Write the new password:')
                create_password = passwd_change
                print('Done')
                exit_or()
        if choose_settings == '2':
            user_change = input('Enter your new name: ')
            while user_change == '':
                print('Its empty!')
                user_change = input('Write the new password:')
                user_account = user_change
                exit_or()
        if choose_settings == '3':
            age_change = input('Change your age: ')
            while age_change == '':
                print('Its empty!')
                age_change = input('Change your age: ')
                login_age = age_change
                exit_or()
                break