import random
import All.sign_in as sign_in
import All.menu as menu
sign_in.sign_in
print('-'*40)
menu.school_menu()

choose_school_menu = input('Choose your option: ')

if choose_school_menu == '1':
    print(menu.school_1manager.Manager_display())
    print(menu.school_2manager.Manager_display())
    print(menu.superviser.Manager_display())
    
elif choose_school_menu == '2':
    print('------There are 5 teachers in our school------')

    print(menu.teacher_1.Teacher_display())
    print(menu.teacher_2.Teacher_display())
    print(menu.teacher_3.Teacher_display())
    print(menu.teacher_4.Teacher_display())
    print(menu.teacher_5.Teacher_display())

elif choose_school_menu == '3':
    print(menu.school_1.school_display())
elif choose_school_menu == '4':
    choose = input('Choose your payment method|1.cash|2.credit card: ')
    if choose == '1':
        print('You have chosen cash')
    elif choose == '2':
        print('You have chosen credit card')
    else:
        print('Invalid choice')
        exit()
elif choose_school_menu == '5':
    print('You can contact us via email: 123@email.com')
elif choose_school_menu == '6':
    print('We are a private school located in Cairo, Egypt. Our mission is to provide quality education to our students.')
elif choose_school_menu == '7':
    exit()