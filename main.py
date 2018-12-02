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

def clear():
    clr_men = {'1': ("Erase all teachers", teachers),
               '2': ("Erase all students", students),
               '3': ('Return to main menu', 'done')}
    for item in sorted(clr_men.keys()):
        print(item + ': ' + clr_men[item][0])

    clr_ans = input("Make a selection:")
    clr = clr_men.get(clr_ans)[1]
    if clr != 'done':
        confirm = input("This action will erase all items in this group. Are you sure you want to do that? (y/n)")

        if confirm == 'y':
            clr.clear()

def get_student_by_id():
    pwrs_id = input("Enter student's PowerSchool Id Number:")
    for stud in students:
        if pwrs_id == stud.pwrs_id:
            return stud
    return "Student not found."


def get_student_by_fl():
    fl = " " + input("Enter student's first and last name:")
    for stud in students:
        if fl == stud.fname + ' ' + stud.lname:
            return stud
    return "Student not found."


def students_by_class(cl):
    class_roster = []
    for student in students:
        if cl in student:
            pass


def student_lookup():
    s_l = {'1' : ('Look up by PowerSchool Id Number', get_student_by_id),
           '2': ('Look up by first and last name', get_student_by_fl),
           '3' : ('Finished', 'done')}

    for item in sorted(s_l.keys()):
        print(item + ":" + s_l[item][0])

    ans = input("Make a selection:")

    found = False

    while not found:
        student = s_l.get(ans)[1]()
        print("======================================")
        print(student)
        print("======================================")
        if type(student) == Student:
            found = True

def gen_report(rep):
    print('======================================')
    i = 0
    for things in rep:
        i += 1
        print(things)
        print("======================================")


def edit_student():

    stud = get_student_by_fl()
    ed_men = {'1': ('Add class.', stud.add_class),
              '2': ('Add parent.', get_student_by_fl),
              '3': ('Finished', 'done')}

    for item in sorted(ed_men.keys()):
        print(item + ":" + ed_men[item][0])

    ans = input("Make a selection:")

    if ans == "1":
        print("Add Class")
        cl = input("Class:")
        ed_men.get(ans)[1](cl)


menu = {'1': ('New Behavior Report', create_behavior),
        '2': ('New Zap Report', create_zap),
        '3': ('Lookup Student', student_lookup),
        '4': ('Edit Student', edit_student),
        '5': ('Import Students from CSV', import_students),
        '6': ('Add new teacher', add_teacher),
        '7': ('Generate Report', report),
        '8': ('Clear List', clear),
        '9': ('Quit', pro_exit)}

run = True

while run:

    for item in sorted(menu.keys()):
        print(item + ': ' + menu[item][0])

    ans = input("Make a selection: ")

    menu.get(ans)[1]()
