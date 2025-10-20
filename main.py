import json

def load_students():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_students(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

def mark_attendance(students):
    for student in students:
        present = input(f"Is {student} present? (y/n): ")
        students[student].append("Present" if present.lower() == "y" else "Absent")
    save_students(students)

def main():
    students = load_students()
    if not students:
        n = int(input("Enter number of students: "))
        for _ in range(n):
            name = input("Enter student name: ")
            students[name] = []
        save_students(students)
    mark_attendance(students)
    print("Attendance updated!")

if __name__ == "__main__":
    main()
