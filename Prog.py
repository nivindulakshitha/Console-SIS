import os, time

def print_menu():
	global menu
	print(menu, end="")

def get_student_id(keyword=""):
	global students, ids

	while True:
		student_id = input(f"   ({keyword})[Student ID]: ")
		if ids.count(student_id) == 0:
			print(f"'{student_id}' not found.")
		else:
			break
		
	return student_id

def register_student():
	global students, ids
	student = {"Student ID": "", "Name": "", "Age": 0, "Grade": 0}

	for key in student.keys():
		value = input(f"   (NEW)[{key.title()}]: ")

		if key == "Student ID":

			while ids.count(value) > 0:
				value = input(f"   (NEW)[{key.title()}]: ")
			else:
				student.update({key: value})

		else:
			if key in ("Age", "Grade"):
				student.update({key: int(value)})
			else:
				student.update({key: value.title()})

	students.update({student.get("Student ID"): student})
	ids.append(student.get("Student ID"))

	print("Student registered successfully.")
	time.sleep(1)

def update_student():
	global students, ids
	
	student_id = get_student_id("UPD")
	student = students.get(student_id)

	for key in student.keys():
		if key == "Student ID":
			continue
		
		value = input(f"   (UPD)[{key.title()}]: ")
		
		if key in ("Age", "Grade"):
			student.update({key: int(value)})
		else:
			student.update({key: value.title()})

	students.update({student_id: student})
	print("Student information updated successfully.")
	time.sleep(1)

def remove_student():
	global students, ids
	
	student_id = get_student_id("REM")

	for key, value in students.get(student_id).items():
		if key == "Student ID":
			continue
		print(f"   [{key.title()}]: {value}")

	is_confirmed = input("Are you sure you want to remove this student? (y/n): ")

	if is_confirmed.lower() == "y":
		students.pop(student_id)
		ids.remove(student_id)
		print("Student removed successfully.")
	else:
		print("Operation cancelled.")
	time.sleep(1)

def add_mark(student_id):
	global students, ids, students_marks

	subjects = {"Mathematics": 0, "Science": 0, "English": 0, "Sinhala": 0}

	for key in subjects.keys():
		while True:
			mark = int(input(f"   ({student_id})[{key.title()}]: "))
			if mark < 0 or mark > 100:
				print("Invalid mark. Please enter a valid mark.")
			else:
				break

		subjects.update({key: mark})

	students_marks.update({student_id: subjects})
	print("Subject marks updated successfully.")

def update_mark(student_id):
	global students, ids, students_marks

	subjects = {"Mathematics": 0, "Science": 0, "English": 0, "Sinhala": 0}
		
	for key in subjects.keys():
		while True:
			mark = int(input(f"   ({student_id})[{key.title()}]: "))
			if mark < 0 or mark > 100:
				print("Invalid mark. Please enter a valid mark.")
			else:
				break

		subjects.update({key: mark})

	students_marks.update({student_id: subjects})
	print("Subject marks updated successfully.")

def add_update_mark():
	global students, ids, students_marks

	print("   1. Add Mark\n   2. Update Mark")
	option = int(input("Select Option: "))

	if option == 1 or option == 2:
		student_id = get_student_id("MRK")
	else:
		print("Invalid option.")
		time.sleep(1)
		return

	if option == 1:
		add_mark(student_id)

	elif option == 2:
		update_mark(student_id)

	time.sleep(1)

def get_marks_grade(mark):
	if mark >= 90:
		return "A+"
	elif mark >= 80:
		return "A"
	elif mark >= 70:
		return "B"
	elif mark >= 60:
		return "C"
	else:
		return "F"

def view_student():
	global students, ids

	student_id = get_student_id("VIW")
	student = students.get(student_id)

	for key, value in student.items():
		print(f"   [{key.title()}]: {value}")

	if students_marks.get(student_id) != None:
		for key, value in students_marks.get(student_id).items():
			if key == "Student ID":
				continue
			grade = get_marks_grade(value)
			print(f"   [{key.title()}]: {value} ({grade})")
	else:
		print("   [Marks]: No marks available.")
	
	time.sleep(1)
	input("Press Enter key to continue...")

students = {}
students_marks = {}
ids = []
menu = """
### ABC NATIONAL SCHOOL ###
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
	
	elif feature == 3:
		add_update_mark()

	elif feature == 4:
		remove_student()

	elif feature == 5:
		view_student()

	else:
		if feature != 6:
			print("Selected feature is not available.")
		print("Exiting system...")
		break