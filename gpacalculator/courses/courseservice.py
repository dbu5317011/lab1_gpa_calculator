courses = {}  # Store course_code : {name, credit}

def register_course(code, name, credit):
    courses[code] = {"name": name, "credit": credit}

def list_courses():
    return courses

def get_course(code):
    return courses.get(code)

def course_menu():
    print("\n--- COURSES ---")
    print("Registered courses:")
    for code, data in courses.items():
        print(f"{code} : {data['name']} ({data['credit']} units)")

    code = input("Enter new Course Code: ")
    name = input("Enter Course Name: ")
    credit = int(input("Enter Credit Units: "))

    register_course(code, name, credit)
    print("Course registered successfully.")
