school_1manager = 'amgad ahmed saad'.title()
school_2manager = 'mahmoud abdelrahmen mohamed'.title()
superviser = 'kholod elezaby barakat'.title()

class Managers:
    def __init__(self,age,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def Manager_display(self):
        return self.first_name,self.last_name,self.age
    
school_1manager = Managers(first_name='Amged',last_name='Saad',age=33)
school_2manager = Managers(first_name='Mahmoud',last_name='Mohamed',age=21)
superviser = Managers(first_name='Kholod',last_name='Barakat',age=19)


class Teachers:
    def __init__(self,age,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def Teacher_display(self):
        return self.first_name,self.last_name,self.age

teacher_1 = Teachers(first_name='Ahmed',last_name='Saad',age=19)
teacher_2 = Teachers(first_name='Mahmoud',last_name='Fady',age=52)
teacher_3 = Teachers(first_name='Khaled',last_name='Danial',age=45)
teacher_4 = Teachers(first_name='Ali',last_name='Mosaad',age=38)
teacher_5 = Teachers(first_name='Foad',last_name='Mar3y',age=28)


class school_details:
    def __init__(self,school_name,school_location,school_type):
        self.school_name = school_name
        self.school_location = school_location
        self.school_type = school_type

    def school_display(self):
        return self.school_name,self.school_location,self.school_type

school_1 = school_details(school_name='Al-Azhar',school_location='Cairo',school_type='Private') 



def school_menu():
    print('1.Managers')
    print('2.Teachers')
    print('3.School details')
    print('4.Payments')
    print('5.Contacts')
    print('6.About us')
    print('7.Exit')

