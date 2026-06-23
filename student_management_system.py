students=[]

def add_student():
    name=input("Enter student name: ")
    age=input("Enter student age: ")
    marks=input("Enter student marks: ")
    student={
        "name":name,"age":age,"marks":marks
    }
    students.append(student)
    print("student added successfully")

def view_student():
    if len(students)==0:
        print("No students found")
    print("students record")
    for student in students:
        print("------------------")
        print("name: ",student["name"])
        print("age: ",student["age"])
        print("marks: ",student["marks"])

def search_student():
    search=input("Enter student name: ")
    found=False

    for student in students:
        if search.lower()==student["name"].lower():
            print("student found")
            print("name: ",student["name"])
            print("age: ",student["age"])
            print("marks: ",student["marks"])
            found=True
            break
    if not found:
        print("student not found")

def save_to_file():
    file = open("students.txt", "w")

    for student in students:
        file.write(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Mark: {student['marks']}\n"
        )

    file.close()
    print("Data saved to students.txt")

def delete_student():
    delete_student=input("Enter student name to delete: ")
    found=False
    for student in students:
        if delete_student.lower()==student["name"].lower():
            students.remove(student)
            found=True
            print("student deleted")
            break
    if not found:
        print("student not found")

def update_student():
    update_student=input("Enter student name to update: ")
    found=False
    for student in students:
        if update_student.lower()==student["name"].lower():
            student["marks"]=input("Enter student marks: ")
            student.update({"mark":student["marks"]})
            found=True
            print("student mark updated successfully")
            break
    if not found:
        print("student not found")

def highest_mark():
    highest=students[0]
    for student in students:
        if student["marks"]>highest["marks"]:
            highest=student
    print("highest mark: ",highest["marks"])
    print("student: ",highest["name"])

def total_student():
    total=0
    for student in students:
        total=total+1
    print("total students: ",total)


while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Search students")
    print("4. Save to files")
    print("5. Delete student")
    print("6. Update student")
    print("7. Highest mark")
    print("8. Total student")
    print("9. Exit")


    choice=int(input("Enter your choice: "))
    
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        save_to_file()
    elif choice==5:
        delete_student()
    elif choice==6:
        update_student()
    elif choice==7:
        highest_mark()
    elif choice==8:
        total_student()
    elif choice==9:
        print("Thank you for using this program,Exiting..")
        break
    else:
        print("Invalid choice")





