from results.resultservice import get_results
from courses.courseservice import get_course

grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

def calculate_gpa(student_id):
    results = get_results(student_id)
    if not results:
        return 0, 0, 0.0

    total_credit = 0
    total_grade_points = 0

    for course_code, grade in results.items():
        course = get_course(course_code)
        if course:
            credit = course["credit"]
            gp = grade_points.get(grade.upper(), 0)

            total_credit += credit
            total_grade_points += gp * credit

    gpa = total_grade_points / total_credit if total_credit > 0 else 0
    return total_credit, total_grade_points, gpa

def grade_report_menu():
    print("\n--- GRADE REPORT MENU ---")
    student_id = input("Enter Student ID: ")
    total_credit, total_gp, gpa = calculate_gpa(student_id)
    print("\n--- GRADE REPORT ---")
    print(f"Total Credits: {total_credit}")
    print(f"Total Grade Points: {total_gp}")
    print(f"GPA: {gpa:.2f}")
