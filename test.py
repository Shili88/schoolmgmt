"""
1. student 
2. teacher 
3. homeroom teacher

4. create - start the user creation process.
5. manage - should start the user management process.
6. end
"""

COMMAND_LIST_MSG = """Available commands:
- create - to cerate the user for students, teacher or homeroom_teacher
- manage - to manage the user 
- end - to end the system
"""

# {"class_number"}: {"student": []}, "teacher": [], "homeroom_teacher" []
school = {} 

# Class for student system
class Student:
    def __init__(self, first_name, last_name, class_number):
        self.first_name = first_name
        self.last_name = last_name
        self.class_number = class_number

#Class for teacher system
class Teacher:
    def __init__(self, name):
        self.name = ...
        self.subject = ...
        self.calss_number = ...

#Class for homeroom teacher system
class Homeroom_teacher:
    def __init__(self, name):
        self.name = ...
        self.subject = ...
        self.calss_number = ...

while True:
    print("Hello user, welcome to the school management system.")
    print("-" * 20)
    print(COMMAND_LIST_MSG)
    command_action = input("Please select the command you wish to proceed: ")
    print("-" * 20)
    print(f"You have selected '{command_action}'. Proceed.....")

# End function 
    if command_action == "end":
        print("Ending the system.....")
        break

# Create function 
    elif command_action == "create":
        print("Enter 1 to add student, 2 for teacher, 3 for homeschool teacher")
        print("-" * 20)
        type_to_add = input()
        print(f"You have selected number '{type_to_add}'. Moving to the selected system now....")
        print("-" * 20)

        if type_to_add == "1":
            print("You are on the student management system.")
            sfirst_name = input("Please enter the first name: ")
            slast_name = input("Please enter the last name: ")
            sclass_number = input ("Please enter the class number: ")
            print("-" * 20)
            # refer to the class
            new_student = Student(first_name=sfirst_name, last_name=slast_name, class_number=sclass_number)
            # refer to the dictionary 
            if sclass_number not in school:
                school[sclass_number] = {"student": [], "teacher": [], "home teacher": None}
            print("-" * 20)
            # track the history 
            school[sclass_number]["student"].append(new_student)

        elif type_to_add == "2":
            print("You are on the teacher management system.")
        else:
            print("You are on the home teacher management system.")
    
    elif command_action == "manage":
        print("Managing....")
    
    else:
        print(f"The command action '{command_action}' you have selected is not available. Please re-select it.")