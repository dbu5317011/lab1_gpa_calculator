students = {}  # Store student_id : {name: ...}

def register_student(student_id, name):
    students[student_id] = {"name": name}

def get_student(student_id):
    return students.get(student_id)

def list_students():
    return students

def student_menu():
    print("\n--- STUDENTS ---")
    print("Registered students:")
    for sid, data in students.items():
        print(f"{sid} : {data['name']}")

    sid = input("Enter new Student ID: ")
    name = input("Enter Student Name: ")
    register_student(sid, name)

    print("Student registered successfully.")
