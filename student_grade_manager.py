student={}
def menu():
    print("\n--- STUDENT MANAGER ---")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Exit")

def add_student():
    name=input ("Enter student name:")

    try:
        grade=float (input("Enter student grade:"))

        if grade<0 or grade >100:
            print("invalid grade")
            return
        
        student[name]=grade

        print("student added")

    except ValueError:
        print("invalid grade")

def view_students():
    if not student:
        print("no students found")
        return
    
    for name in student:
        print(f"Name: {name} | Grade: {student[name]}")

def search_student():
    name=input("enter student name:")

    if name in student:
        print(f"Grade: {student[name]}")
    else:
        print("student not found")

while True:
    menu()
    option=input("choose an option:")

    if option=="1":
        add_student()
    elif option=="2":
        view_students()
    elif option=="3":
        search_student()
    elif option=="4":
        print("goodbye")
        break
    else:
        print("invalid option")
