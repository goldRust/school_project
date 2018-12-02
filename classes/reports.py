from classes.people import Student
from classes.people import Teacher
from classes.people import Class

class Zap:
    def __init__(self, Student, Class, assignment, Teacher):
        self.student = Student
        self.cl = Class
        self.assignment = assignment
        self.teacher = Teacher

class Behavior:
    def __init__(self, Student, Class, beh, Teacher):
        self.student = Student
        self.cl = Class
        self.beh = beh
        self.teacher = Teacher