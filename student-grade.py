#initalizing dictionary
uiet_grade = { }

#add a new student 
def add_student(name,grade):
    uiet_grade[name] = grade
    print(f"Added{name} with a {grade}")

#update a student 
def update_student(name,grade):
    if name in uiet_grade:
        uiet_grade[name] = grade
        print(f"{name}with marks are updated{grade}")

    else:
        print(f"{name}is not found!")
#delete a student 
def delete_student(name):
    if name in uiet_grade:
        del uiet_grade[name]
        print(f"{name}has been successfully deleted")
    else:
        print(f"{name}is not found!")
#view all student
def display_all_student():
    if uiet_grade:
        for name, grade in uiet_grade.items():
            print(f"{name} : {grade}")

    else:
        print("no student found\added")

def main():
    while True:
        print('\n student grades management system')
        print("1. add student")
        print("2. update student")
        print("3. deleted student")
        print("4. view student")
        print("5. exit")
        choice = int(input("enter your choice = "))
        if choice ==1:
            name=input("enter student name = ")
            grade = int(input("enter student grade = "))
            add_student(name,grade)
        elif choice ==2:
            name = input("enter student name: ")
            grade = int(input("enter student grade = "))
            update_student(name,grade) 
        elif choice==3:
            name=input("enter student name = ")
            delete_student(name) 
        elif choice==4:
            display_all_student()
        elif choice ==5:
            print("clossing the programe...")
            break
        else:
            print("invailid choice")                 
        
main()
