

"""

    Topic: Student Class
    Date: 31 Oct 2023
    Author: Sarah

    
"""


class Student:

    ### Class Level Attributes
    __counter = 0
    
    ### Constructor
    def __init__(self, fName=None, lName=None, age=0):
        

        
        ### Instance Level Attributes
        self.__firstName = fName
        self.__lastName = lName
        self.__age = age
        Student.__counter += 1

            


    ### Instance Level Methods

    @property
    def getFirstName(self):
        return self.__firstName

    @getFirstName.setter
    def setFirstName(self, fName):

        if fName == None or fName.isdigit() or fName.isspace():
            print(f"Error: {fName} value cannot be used for the first name.")
        else:
            self.__firstName = fName

    @property
    def getLastName(self):
        return self.__lastName

    @getLastName.setter
    def setLastName(self, lName):

        if lName == None or lName.isdigit() or lName.isspace():
            print(f"Error: {lName} value cannot be used for the last name.")
        else:
            self.__lastName = lName

    @property
    def getAge(self):
        return self.__age

    @getAge.setter
    def setAge(self, age):

        if age == None or age > 80 or age < 18:
            print(f"Error: {age} value cannot be used for the age.")
        else:
            self.__age = age


    
    def tellMeAboutYourself(self):
        print(f"My name is {self.__lastName}, {self.__firstName} and I have {self.__age} years old.")


    #### Class Level Method
    @classmethod
    def getTotalObj(cls):
        print(f"The total number opf students are {cls.__counter}.")

        














    

####        

