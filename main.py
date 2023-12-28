

"""

    This is the main file to give access the user
    Topic: OOP
    Date: 31 Oct  2023
    Author: Sarah


"""
from student import Student

        

if __name__ == "__main__":

    print("+++++++++++++++++++++++ First Student Object")

    s1 = Student("James", "Jones", 22)
    
    ##s1.setFirstName("James")
    ##s1.setLastName("Jones")
    ##s1.setAge(22)

    s1.tellMeAboutYourself()
    

    print("\n\n+++++++++++++++++++++++ Second Student Object")
    ### Fully Parameterized Constructor
    s2 = Student("Shelly", "Williams", 25)

    ##s2.setFirstName("Shelly")
    ##s2.setLastName("Williams")
    ##s2.setAge(25)

    s2.tellMeAboutYourself()

    print("\n\n+++++++++++++++++++++++ let's modify Student Object")

    s2.setLastName = " "
    s2.setAge = 2500

    s2.tellMeAboutYourself()

    print("\n\n+++++++++++++++++++++++ Third Student Object")
    ### Fully Parameterized Constructor
    s3 = Student(age=26, fName="Mike", lName="Dean")
    s3.tellMeAboutYourself()

    print("\n\n+++++++++++++++++++++++ Fourth Student Object")

    ### Default Constructor
    s4 = Student()
    s4.tellMeAboutYourself()

    s4.setFirstName = "Marry"
    s4.setLastName = "Jones"
    s4.setAge =  27

    s4.tellMeAboutYourself()

    print("\n\n+++++++++++++++++++++++ Fifth Student Object")
    ### Partially Parameterized Constructor
    s5 = Student(fName="Micheal", age=32)
    s5.tellMeAboutYourself()

    s5.setLastName= "Jordan"

    s5.tellMeAboutYourself()


    print("\n\n+++++++++++++++++++++++ Sixth Student Object")
    
    s6 = Student()

    ##s6.getTotalObj()
    Student.getTotalObj()
    ##s1.getTotalObj()
    ##s4.getTotalObj()

    #### 1
    #### 6

    

    

    


    """
        Copy Constructor

        --- Factory Method


    """
    

"""
    Access Modifier
    - priavte: the scope of visibility is only inside of the class
    - protected: the scope of visibility will be between children that they 
               are going to inherit from a class
    - Package/Default: the scope of visibility will be between the classes that \
                    they exist in the same location

    - Public: the scope of visibility is public to everyone
"""


























    


    
