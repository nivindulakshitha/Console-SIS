import os

def print_menu():
	global menu
	print(menu, end="")

def register_student():
	global students, ids
	student = {"Student ID": "", "Name": "", "Age": 0, "Grade": 0}

	for key in student.keys():
		value = input(f"   [{key.lower()}]: ")

		if key == "Student ID":

			while ids.count(value) > 0:
				value = input(f"   [{key.lower()}]: ")
			else:
				student.update({key: value})

		else:
			if key in ("Age", "Grade"):
				student.update({key: int(value)})
			else:
				student.update({key: value})
	
	students.update({student.get("Student ID"): student})
	ids.append(student.get("Student ID"))

students = {}
ids = []
menu = """
School Management System

1. Register New Student
2. Update Student Information
3. Add/Update Subject Mark
4. Remove Student
5. View Student Details
6. Exit System

"""

while True:
	os.system('cls')
	print_menu()

	feature = int(input("Select Option: "))

	if feature == 6:
		break
	
	if feature == 1:
		register_student()