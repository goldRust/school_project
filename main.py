import pickle
import csv
from classes.people import Teacher
from classes.people import Student

teachers = pickle.load(open('testpkl.p', 'rb'))
students = pickle.load(open('students.p', 'rb'))


def add_teacher():
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    user = input("User Name: ")
    password = input("New Password: ")

    new_teacher = Teacher(last_name, first_name, user, password)
    teachers.append(new_teacher)
    new_teacher.add_class()

    with open('testpkl.p', 'wb') as file:
        pickle.dump(teachers, file)


def create_behavior():
    print('Everything runs.')
    pass


def create_zap():
    pass


def import_students():
    with open('students.csv') as csv_file:
        student_maker = csv.reader(csv_file)

        for stud in student_maker:

            new_stud = Student(stud[0], stud[1], stud[2])
            print(new_stud)

            if new_stud not in students:
                students.append(new_stud)
                print("Added student:  " + new_stud.fname + new_stud.lname)
            else:
                print("That student already exists.")

    delete_duplicates(students)

    with open ('students.p', 'wb') as file:
        pickle.dump(students, file)


def delete_duplicates(list):
    for item in list:
        num = 0
        for second in list:
            if item == second:
                num += 1
        if num == 2:
            list.remove(item)

    pass


def add_student():
    pass


def pro_exit():
    print("Good bye.")
    exit()


def report():
    rep_men = {'1': ("List teachers", teachers),
               '2': ("List students", students),
               '3': ('Return to main menu', 'done')}
    for item in sorted(rep_men.keys()):
        print(item + ': ' + rep_men[item][0])

    rep_ans = input("Make a selection:")
    rep = rep_men.get(rep_ans)[1]
    if rep != 'done':
        gen_report(rep)


def gen_report(rep):
    print('======================================')
    i = 0
    for things in rep:
        i += 1
        print(str(i)+':' + things.lname + ", " + things.fname)
        print("======================================")


menu = {'1': ('New Behavior Report', create_behavior),
        '2': ('New Zap Report', create_zap),
        '3': ('Add new student', add_student),
        '4': ('Import Students from CSV', import_students),
        '5': ('Add new teacher', add_teacher),
        '6': ('Generate Report', report),
        '7': ('Quit', pro_exit)}

run = True

while run:

    for item in sorted(menu.keys()):
        print(item + ': ' + menu[item][0])

    ans = input("Make a selection: ")

    menu.get(ans)[1]()
