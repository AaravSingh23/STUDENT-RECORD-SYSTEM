import pickle
import os

FILE_NAME = "students.dat"


class Student:
    def __init__(self, college, name, roll_no,
                 maths, physics, chemistry,
                 biology, hindi):

        self.college = college
        self.name = name
        self.roll_no = roll_no

        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.hindi = hindi

        self.total = maths + physics + chemistry + biology + hindi
        self.percentage = self.total / 5


def load_records():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except:
        return []


def save_records(records):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(records, file)


def add_student():

    records = load_records()

    roll_no = int(input("Enter Roll Number: "))

    for student in records:
        if student.roll_no == roll_no:
            print("Error: Roll Number Already Exists!")
            return

    college = input("Enter School/College Name: ")
    name = input("Enter Student Name: ")

    maths = float(input("Enter Maths Marks: "))
    physics = float(input("Enter Physics Marks: "))
    chemistry = float(input("Enter Chemistry Marks: "))
    biology = float(input("Enter Biology Marks: "))
    hindi = float(input("Enter Hindi Marks: "))

    student = Student(
        college,
        name,
        roll_no,
        maths,
        physics,
        chemistry,
        biology,
        hindi
    )

    records.append(student)

    records.sort(key=lambda x: x.roll_no)

    save_records(records)

    print("\nStudent Record Added Successfully!")


def display_students():

    records = load_records()

    if not records:
        print("No Records Found!")
        return

    print("\n========== ALL STUDENT RECORDS ==========\n")

    for s in records:

        print(f"College Name : {s.college}")
        print(f"Student Name : {s.name}")
        print(f"Roll Number  : {s.roll_no}")

        print(f"Maths        : {s.maths}")
        print(f"Physics      : {s.physics}")
        print(f"Chemistry    : {s.chemistry}")
        print(f"Biology      : {s.biology}")
        print(f"Hindi        : {s.hindi}")

        print(f"Total Marks  : {s.total}")
        print(f"Percentage   : {s.percentage:.2f}%")

        print("-" * 40)


def binary_search(records, roll_no):

    low = 0
    high = len(records) - 1

    while low <= high:

        mid = (low + high) // 2

        if records[mid].roll_no == roll_no:
            return records[mid]

        elif records[mid].roll_no < roll_no:
            low = mid + 1

        else:
            high = mid - 1

    return None


def search_student():

    records = load_records()

    if not records:
        print("No Records Found!")
        return

    roll_no = int(input("Enter Roll Number To Search: "))

    student = binary_search(records, roll_no)

    if student:

        print("\n========== RECORD FOUND ==========\n")

        print("College Name :", student.college)
        print("Student Name :", student.name)
        print("Roll Number  :", student.roll_no)

        print("Maths        :", student.maths)
        print("Physics      :", student.physics)
        print("Chemistry    :", student.chemistry)
        print("Biology      :", student.biology)
        print("Hindi        :", student.hindi)

        print("Total Marks  :", student.total)
        print("Percentage   :", round(student.percentage, 2), "%")

    else:
        print("Record Not Found!")


def delete_student():

    records = load_records()

    if not records:
        print("No Records Found!")
        return

    roll_no = int(input("Enter Roll Number To Delete: "))

    for student in records:

        if student.roll_no == roll_no:

            records.remove(student)

            save_records(records)

            print("Record Deleted Successfully!")
            return

    print("Record Not Found!")


def update_student():

    records = load_records()

    if not records:
        print("No Records Found!")
        return

    roll_no = int(input("Enter Roll Number To Update: "))

    found = False

    for student in records:

        if student.roll_no == roll_no:

            print("\nCurrent Details:")
            print("College Name :", student.college)
            print("Student Name :", student.name)
            print("Maths :", student.maths)
            print("Physics :", student.physics)
            print("Chemistry :", student.chemistry)
            print("Biology :", student.biology)
            print("Hindi :", student.hindi)

            print("\nEnter New Details")

            student.college = input("Enter College Name: ")
            student.name = input("Enter Student Name: ")

            student.maths = float(input("Enter Maths Marks: "))
            student.physics = float(input("Enter Physics Marks: "))
            student.chemistry = float(input("Enter Chemistry Marks: "))
            student.biology = float(input("Enter Biology Marks: "))
            student.hindi = float(input("Enter Hindi Marks: "))

            student.total = (
                student.maths +
                student.physics +
                student.chemistry +
                student.biology +
                student.hindi
            )

            student.percentage = student.total / 5

            save_records(records)

            print("\nRecord Updated Successfully!")

            found = True
            break

    if not found:
        print("Record Not Found!")


def main():

    while True:

        print("\n========== STUDENT RECORD SYSTEM ==========")
        print("1. Add Student Record")
        print("2. Display All Students")
        print("3. Search Student by Roll Number")
        print("4. Delete Student Record")
        print("5. Update Student Record")
        print("6. Exit")

        choice = input("Enter Choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Please Enter 1-6")


if __name__ == "__main__":
    main()