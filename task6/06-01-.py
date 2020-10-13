#!/usr/bin/env python

from datetime import datetime
import string
from random import *

class Student:
    """Data for init class student"""
    
    def __init__(self, name='Ivan', surname='Petrov',birthday='01.02.2001', gender='Male', grade=5, speciality='System ingenier', course=3):
    
        self.__setname(name)    
        self.__setsurname(surname)   
        self.__setbirthday(birthday)   
        self.__setgender(gender)     
        self.__setgrade(grade)      
        self.__setspeciality(speciality) 
        self.__setcourse(course)     


    #Name must be no more 25 chars length. RO.    
    @property
    def name(self):    return self.__name

    def __setname(self, value):
        if isinstance(value, str):
            if len(value) <= 25:
                self.__name = value
            else:
                raise ValueError("Name must be no more 25 chars length.")
        else:
            raise ValueError("Name must be a string.")


    #Surname must be no more 50 chars length. RO.       
    @property
    def surname(self):    return self.__surname

    def __setsurname(self, value):
        if isinstance(value, str):
            if len(value) <= 50:
                self.__surname = value
            else:
                raise ValueError("Surname must be no more 50 chars length.")
        else:
            raise ValueError("Surname must be a string.")
    
    
    #Birthday date format 'dd.mm.yyyy'. RO.
    @property
    def birthday(self):    return self.__birthday

    def __setbirthday(self, value):
        try:
#            datetime.strptime(value, '%d.%m.%Y')
            datetime.strptime(value, '%Y-%m-%d')
        except:
#            raise ValueError("Birthday date format input error. Must be 'dd.mm.yyyy'.")
            raise ValueError("Birthday date format input error. Must be 'yyyy-mm-dd'.")
        self.__birthday = value
    
    
    #Gender can be one of two: Male or Female. RO.
    @property
    def gender(self):    return self.__gender

    def __setgender(self, value):
        if (value == 'Male') | (value == 'Female'):
            self.__gender = value
        else:
            raise ValueError("Gender can be one of two: Male or Female.")
    
    
    #Grade must be number from 1 to 10.
    @property
    def grade(self):    return self.__grade
    @grade.setter
    def grade(self, value):       self.__setgrade(value)    
    
    def __setgrade(self, value):
        if isinstance(value, int):
            if value in range(0, 11):
                self.__grade = value
            else:
                raise ValueError("Grade must be number from 1 to 10.")
        else:
            raise ValueError("Grade must be number from 1 to 10.")    
    

    #Specialty must be no more 50 chars length. RW.
    @property
    def speciality(self):    return self.__speciality
    @speciality.setter
    def speciality(self, value):  self.__setspeciality(value)

    def __setspeciality(self, value):
        if isinstance(value, str):
            if len(value) <= 50:
                self.__speciality = value
            else:
                raise ValueError("Specialty must be no more 50 chars length.")
        else:
            raise ValueError("Specialty must be a string.")    
    

    #Course must be integer number. RW.
    @property
    def course(self):    return self.__course
    @course.setter
    def course(self, value):      self.__setcourse(value)
    
    def __setcourse(self, value):
        if isinstance(value, int):
                self.__course = value
        else:
            raise ValueError("Course must be integer number.")    
    


    def __str__(self):
        return("|Student: {} {} | Birthday: {} | Gender: {} | Grade: {} | Specialty: {} | Course number: {}|\n")\
        .format(self.name, self.surname, self.birthday,self.gender, str(self.grade), self.speciality, str(self.course))
            
    @staticmethod        
    def newStudent(value):
        if isinstance(value, str):
            args = value.split(':')
            if len(args)==7:
                if args[3] == 'M':    args[3] = 'Male'
                elif args[3] == 'F':    args[3] = 'Female'
                else:
                    raise ValueError("Gender can be one of two: M for Male or F for Female.")
                args[4] = int(args[4])
                args[6] = int(args[6])
                return Student( args[0], args[1], args[2], args[3], args[4], args[5], args[6])
            else:
                raise ValueError("Number input parameter must be 7: 'NAME:LASTNAME:BIRTHDATE:GENDER(char M-Male, F-Female):GRADE:SPECIALITY:COURSE_NUMBER'.")
        else:
            raise ValueError("Input string must be 'NAME:LASTNAME:BIRTHDATE:GENDER(char M-Male, F-Female):GRADE:SPECIALITY:COURSE_NUMBER'.")
        

        
class ExtendedStudent(Student):
    
    def __init__(self, name, surname, birthday, gender, grade, speciality, course, login, password):
        super(ExtendedStudent, self).__init__(name, surname, birthday, gender,
            grade, speciality, course)
        self.__setlogin(login)
        self.__setpassword(password)

        
    #Login.
    @property
    def login(self):    return self.__login
    @login.setter
    def login(self, value):  self.__setlogin(value)
    
    def __setlogin(self, value):
        if isinstance(value, str):
            self.__login = value
        else:
            raise ValueError("Login must be a string.")
        
    
    #Password.
    @property
    def password(self):    return self.__password
    @password.setter
    def password(self, value):  self.__setpassword(value)
           
    def __setpassword(self, value):
        if isinstance(value, str):
            self.__password = value
        else:
            raise ValueError("Password must be a string.")
            
            
    def __str__(self):
        return("|Student: {} {} | Birthday: {} | Gender: {} | Grade: {} | Specialty: {} | Course number: {} | Login: {} | Password {}|\n")\
        .format(self.name, self.surname, self.birthday,self.gender, str(self.grade), self.speciality, str(self.course), self.login, self.password)


    @staticmethod
    def newStudent(value):

        if isinstance(value, str):
            args = value.split(':::')
            if len(args)==7:
                if args[3] == 'M':    args[3] = 'Male'
                elif args[3] == 'F':    args[3] = 'Female'
                else:
                    raise ValueError("Gender can be one of two: M for Male or F for Female.")
                args[4] = int(args[4])
                args[6] = int(args[6])
                #Creating login from first char of name and whole surname
                login = ('' + args[0][0] + args[1]).lower()
                #Simbols set for password
                simbols = string.ascii_letters + string.digits
                #Generating password from 6 to 9 chars length
                password = ''.join(choice(simbols) for x in range(randint(6, 9)))
                return ExtendedStudent( args[0], args[1], args[2], args[3], args[4], args[5], args[6], login, password)
            else:
                raise ValueError("Number input parameter must be 7: 'NAME:::LASTNAME:::BIRTHDATE:::GENDER(char M-Male, F-Female):::GRADE:SPECIALITY:::COURSE_NUMBER'.")
        else:
            raise ValueError("Input string must be 'NAME:::LASTNAME:::BIRTHDATE:::GENDER(char M-Male, F-Female):::GRADE:::SPECIALITY:::COURSE_NUMBER'.")

        
    
def main():
    
    infile = open('students.dat', "r")
    outfile = open('extended_students.dat', "w")
    students = {}
    for line in infile.readlines():
        student=ExtendedStudent.newStudent(line)
        #Counting identical logins
        if student.login in students:
            students[student.login]=students[student.login]+1
        else:
            students[student.login]=1
        #Numbering of login
        if students[student.login]>1:
            student.login=student.login+str(students[student.login]-1)
        outfile.write(str(student))
    outfile.close()
    infile.close()

main()