def display_menu():
    print("\n welcome to the student data organizar")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Updqate Student Information")
    print("4. Delete Student")
    print("5. Display Student Offered")
    print("6. Exit")


students = []


def add_students():
    name = input("Enter name: ")
    id = input("Enter id: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    subjects_input = input("Subject name (comma-seperated): ")
    subjects = set(subject.strip() for subject in subjects_input.split(","))

    students_data = {
        "name": name,
        "id": id,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects,
    }

    students.append({id: students_data})
    print("Students add successfully")


def display_students():
    if not students:
        print("No students record found")
    for record in students:
        for id, info in record.items():
            print(
                f"student id:{id}, name:{info['name']}, age:{info['age']}, grade:{info['grade']},  subject:{','.join(info['subjects'])}"
            )


def update_students():
    uid = input("Enter student id to update: ")
    for record in students:
        if uid in record:
            info = record[uid]
            print("1. Update name: ")
            print("2. Update age: ")
            print("3. Update grade: ")
            print("4. Update subjects: ")
            choice = input("enter choice")
            if choice == "1":
                info["name"] = input("Enter name: ")
            elif choice == "2":
                info["age"] = input("Enter age: ")
            elif choice == "3":
                info["grade"] = input("Enter grade: ")
            elif choice == "4":
                info["subject"] = input("Enter subject (comma-sepreted): ")
            print("Student info updated")
            return


def delete_students():
    uid = input("Enter student id to delete: ")
    for index, record in enumerate(students):
        if uid in record:
            del students[index]
            print("delete successfully")
            return
    print("Student not founded")


def display_subjects():
    all_subjects = set()
    for record in students:
        for aa in record.values():
            all_subjects.update(aa["subjects"])
    print("Subjects Offered: ", ", ".join(all_subjects))


while True:
    display_menu()
    option = input("Enter your choice: ")
    if option == "1":
        add_students()
    elif option == "2":
        display_students()
    elif option == "3":
        update_students()
    elif option == "4":
        delete_students()
    elif option == "5":
        display_subjects()
    elif option == "6":
        print("Thank you ")
        break
    else:
        print("Invail option. Try again")
