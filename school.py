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
    def __init__(self, first_name, last_name, class_number, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.class_number = class_number
        self.subjects = subjects

#Class for homeroom teacher system
class Homeroom_teacher:
    def __init__(self, first_name, last_name, class_number):
        self.first_name = first_name
        self.last_name = last_name
        self.class_number = class_number


while True:
    print("Hello user, welcome to the school management system.")
    print("-" * 20)
    print(COMMAND_LIST_MSG)
    command_action = input("Please select the command you wish to proceed: ")
    print(school)
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
            print("-" * 20)
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            class_number = input ("Please enter the class number: ")
            print("-" * 20)
            # refer to the class
            new_student = Student(first_name=first_name, last_name=last_name, class_number=class_number)
            # refer to the dictionary 
            if class_number not in school:
                school[class_number] = {"student": [], "teacher": [], "homeroom_teacher": []}
            print("-" * 20)
            # track the history 
            school[class_number]["student"].append(new_student)

        elif type_to_add == "2":
            print("You are on the teacher management system.")
            print("-" * 20)
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            class_number = input ("Please enter the class number: ")
            subjects = input("Enter the subject name: ")
            print("-" * 20)
            # refer to the class
            new_teacher = Teacher(first_name=first_name, last_name=last_name, class_number=class_number, subjects=subjects)
            # refer to the dictionary 
            if class_number not in school:
                school[class_number] ={"student": [], "teacher": [], "homeroom_teacher": []}
            print("-" * 20)
            # track the history 
            school[class_number]["teacher"].append(new_teacher)

        elif type_to_add == "3":
            print("You are on the homeroom teacher management system.")
            print("-" * 20)
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            class_number = input ("Please enter the class number: ")
            print("-" * 20)
            # refer to the class
            new_homeroom_teacher = Homeroom_teacher(first_name=first_name, last_name=last_name, class_number=class_number)
            # refer to the dictionary 
            if class_number not in school:
                school[class_number] = {"student": [], "teacher": [], "homeroom_teacher": []}
            print("-" * 20)
            # track the history 
            school[class_number]["homeroom_teacher"].append(new_homeroom_teacher)
        else:
            print (f"The '{type_to_add}' you have selected is not applicable.")
    
    elif command_action == "manage":
        print("Please select 1.student 2.teacher 3.homeroom teacher 4.class to see the whole class.")
        option = input("Enter the user you tend to manage: ")
        print("-" * 20)
        print(f"You have selected number '{option}'. Moving to the selected system now....")

        if option == "1":
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            for class_number, class_data in school.items():
                for student in class_data ["student"]:
                    if first_name == student.first_name and last_name == student.last_name:
                        print(f"Name: {first_name}{last_name}, class number {class_number}")
                        for teacher in class_data ["teacher"]:
                            print (f" Teacher: {teacher.first_name}{teacher.last_name}, Subject: {teacher.subjects}")
        
        elif option == "2":
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            for class_number, class_data in school.items():
                for teacher in class_data ["teacher"]:
                    if first_name == teacher.first_name and last_name == teacher.last_name:
                        print(f"Name: {first_name}{last_name}, class number {class_number}, Subjects: {teacher.subjects}")
        
        elif option == "3":
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            for class_number, class_data in school.items():
                for homeroom_teacher in class_data ["homeroom_teacher"]:
                    if first_name == homeroom_teacher.first_name and last_name == homeroom_teacher.last_name:
                        print(f"Name: {first_name}{last_name}")
                        for student in class_data["student"]:
                            print(f"student: {student.first_name} {student.last_name}")
        
        elif option == "4":
            search_class = input ("Enter the class number: ")
            for class_number, class_data in school.items(): 
                for student in school[search_class]["student"]:
                    if search_class == class_number:
                        print(f" Students: {student.first_name}{student.last_name}")
                        for homeroom_teacher in class_data["homeroom_teacher"]:
                            if homeroom_teacher.class_number == class_number:
                                print(f"Homeroom teacher {homeroom_teacher.first_name}{homeroom_teacher.last_name}, class number {class_number}")
       
        else:
            print (f"The '{option}' you have selected is not applicable.")
         
    else:
        print(f"The command action '{command_action}' you have selected is not available. Please re-select it.")