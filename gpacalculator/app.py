from students.studentsservice import student_menu
from courses.courseservice import course_menu
from results.resultservice import results_menu
from grade_report.gradereport import grade_report_menu

def main_menu():
    while True:
        print("\n===== GPA CALCULATOR =====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Reports")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            results_menu()
        elif choice == "4":
            grade_report_menu()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main_menu()
