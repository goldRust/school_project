class Student:



    def __init__(self, lname, fname, pwrs_id):
        self.lname = lname
        self.fname = fname
        self.pwrs_id = pwrs_id
        self.email = self.fname + '.' + self.lname + '@mv330.org'

    def __hash__(self):
        return self.pwrs_id

    def __eq__(self, other):
        return self.pwrs_id == other.pwrs_id

    def __repr__(self):
        return 'student({})'.format(self.pwrs_id)

    def get_classes(self):
        for cl in self.classes:
            i = 0
            i += 1
            print(i, ": ", cl)
    behavior = []
    zap = []
    dob = ''
    sex = ''
    email = ''
    parent = ''

class Teacher:
    classes = []

    def __init__(self, lname, fname, user, password):
        self.lname = lname
        self.fname = fname
        self.user = user
        self.password = password


    def add_class(self):
        self.get_classes()

        add = input("Add a class? (y/n)")

        if add == "y":
            new_class = input("Class: ")
            self.classes.append(new_class)
            self.add_class()



    def get_classes(self):
        i = 0
        for cl in self.classes:

            i += 1
            print(i,":", cl)


class Class:

    name = ''
    teacher = ''
    students = []


class Parent:

    first_name = ""
    last_name = ''
    home_phone = ''