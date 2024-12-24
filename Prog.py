import os, time

def print_menu():
	global menu
	print(menu, end="")

def register_student():
	global students, ids
	student = {"Student ID": "", "Name": "", "Age": 0, "Grade": 0}

	for key in student.keys():
		value = input(f"   (new)[{key.lower()}]: ")

		if key == "Student ID":

			while ids.count(value) > 0:
				value = input(f"   (new)[{key.lower()}]: ")
			else:
				student.update({key: value})

		else:
			if key in ("Age", "Grade"):
				student.update({key: int(value)})
			else:
				student.update({key: value})
	
	students.update({student.get("Student ID"): student})
	ids.append(student.get("Student ID"))
	print("Student registered successfully.")
	time.sleep(1)

def update_student():
	global students, ids
	
	while True:
		student_id = input("[student id]: ")
		if ids.count(student_id) == 0:
			print(f"'{student_id}' not found.")
			student_id = input("   [student id]: ")
		else:
			break
		
	student = students.get(student_id)

	for key in student.keys():
		if key == "Student ID":
			continue
		
		if key in ("Age", "Grade"):
			student.update({key: int(input(f"   (UPD)[{key.lower()}]: "))})
		else:
			student.update({key: input(f"   (UPD)[{key.lower()}]: ")})

	students.update({student_id: student})
	print("Student information updated successfully.")
	time.sleep(1)

def remove_student():
	global students, ids
	
	while True:
		student_id = input("   (REM)[student id]: ")
		if ids.count(student_id) == 0:
			print(f"'{student_id}' not found.")
		else:
			break

	for key, value in students.get(student_id).items():
		if key == "Student ID":
			continue
		print(f"   [{key.lower()}]: {value}")

	is_confirmed = input("Are you sure you want to remove this student? (y/n): ")

	if is_confirmed.lower() == "y":
		students.pop(student_id)
		ids.remove(student_id)
		print("Student removed successfully.")
	else:
		print("Operation cancelled.")
	time.sleep(1)

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
	
	if feature == 1:
		register_student()

	elif feature == 2:
		update_student()

	elif feature == 4:
		remove_student()

	else:
		if feature != 6:
			print("Selected feature is not available.")
		break