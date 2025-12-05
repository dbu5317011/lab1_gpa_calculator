from courses.courseservice import courses

results = {}  
# Format: { student_id : { course_code : letter_grade } }

def register_result(student_id, course_code, letter_grade):
    if student_id not in results:
        results[student_id] = {}
    results[student_id][course_code] = letter_grade

def get_results(student_id):
    return results.get(student_id, {})

def results_menu():
    student_id = input("\nEnter Student ID: ")

    print("Existing Results:")
    if student_id in results:
        for course, grade in results[student_id].items():
            print(f"{course}: {grade}")
    else:
        print("No results yet.")

    course_code = input("Enter Course Code: ")
    grade = input("Enter Letter Grade (A-F): ")

    register_result(student_id, course_code, grade)
    print("Result recorded successfully.")
