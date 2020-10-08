#!/usr/bin/env python

from datetime import datetime

class Student:
    """Data for init class student"""
    
    def __init__(self, f='Ivan', l='Petrov', b='01.02.2001', g='Male', c=5, s='System ingenier', n=3):
    
        self.__setname(f)    
        self.__setsurname(l)   
        self.__setbirthday(b)   
        self.__setgender(g)     
        self.__setgrade(c)      
        self.__setspeciality(s) 
        self.__setcource(n)     


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
            datetime.strptime(value, '%d.%m.%Y')
        except:
            raise ValueError("Birthday date format input error. Must be 'dd.mm.yyyy'.")
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
    def course(self, value):      self.__setcource(value)
    
    def __setcource(self, value):
        if isinstance(value, int):
                self.__course = value
        else:
            raise ValueError("Course must be integer number.")    
    


    def __str__(self):
        return("|Student: {} {} | Birthday: {} | Gender: {} | Grade: {} | Specialty: {} | Course number: {}|\n")\
        .format(self.name, self.surname, self.birthday,self.gender, str(self.grade), self.speciality, str(self.course))
            
            
    def newStudent(self, value):
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
        

    
def main():
    st = Student()   
    print(st.__str__())
    st_ka = Student('Maya', 'Alferova', '01.02.2002', 'Female', 10, 'System analist', n=5)
    print(st_ka.__str__())
    entrant = st_ka.newStudent('Leonid:Parfienov:04.05.2006:M:8:Reporter:4')
    print(entrant.__str__()) 
main()