import oop

name = input('Enter your name: ').title()
create_password = input('Create your password: ')
while create_password == '':
    print('Try agian')
    create_password = input('Create your password: ')

confirm_password = input('Confirm your password: ')
while confirm_password == '':
    print('Try agian')
    confirm_password = input('Confirm your password: ')
if confirm_password == create_password:
    create_password = confirm_password
if confirm_password != create_password:
    print('False!')
    quit()

print(f'Hi {name}!') 
print('-'*30)
print('1.Food menu')
print('2.Workers & managers')
print('3.Settings')
choose = input('Choose what you want: ')
if choose == '1':

    menu = {
        1:{'name': 'Rice','price':40},
        2:{'name': 'Chicken','price':290},
        3:{'name': 'Pasta','price':220},
        4:{'name': 'Burger','price':120},
        5:{'name': 'Fries','price':30}
        
    }
    total = 0
    while True:
        command = input(
            "\nType 'menu' to see menu or 'done' to finish: "
        ).lower()
    
        if command == "done":
            break
        
        elif command == "menu":
            for number, item in menu.items():
                print(
                    f"{number}. {item['name']} - "
                    f"{item['price']} EGP"
                )
    
        else:
            print("Please type 'menu' or 'done'.")
            continue
        
        choice = input("Choose item number: ")
    
        if choice.isdigit():
            choice = int(choice)
    
            if choice in menu:
                item = menu[choice]
                total += item["price"]
    
                print("Added:", item["name"])
                print("Item price:", item["price"])
                print("Current total:", total)
            else:
                print("Invalid item number!")
    
        else:
            print("Please enter a number.")
    
    print("\nFinal bill:", total, "EGP")

elif choose == '2':

    print('1.Managers details')
    print('2.Workers details')

    choose2 = input('Choose: ')
    if choose2 == '1':
        print(oop.manager1.Manager_Display())
        print(oop.manager2.Manager_Display())

    elif choose2 == '2':
        print(oop.worker1.Worker_Display())
        print(oop.worker2.Worker_Display())
        print(oop.worker3.Worker_Display())
        print(oop.worker4.Worker_Display())

elif choose == '3':
    print('1.Change password')

    choose3 = input('Choose: ')
while True:
    if choose3 == '1':
        confirm_password = input('Enter your old password: ')
        if confirm_password != create_password:
            print('False!')
        else:
            change_password = input('Write the password u want to change: ')
            confirm_password = change_password
            break

