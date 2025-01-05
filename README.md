# School Management System

This is a Python-based console application for managing student information and their subject marks in a school. It provides features like registering students, updating their information, adding or updating subject marks, and more.

## Features

1. **Register New Student**  
   Allows you to register a new student by providing their ID, name, age, and grade.

2. **Update Student Information**  
   Enables you to update details of an existing student.

3. **Add/Update Subject Marks**  
   Provides options to add marks for a student or update their existing marks.

4. **Remove Student**  
   Allows you to remove a student from the system.

5. **View Student Details**  
   Displays the details of a student, including their subject marks and grades.

6. **Exit System**  
   Exits the application.

---

## Prerequisites

- Python 3.x
- Basic understanding of Python programming

---

## How to Run

1. Save the code in a `.py` file (e.g., `school_management.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script using the command:
   ```bash
   python school_management.py
   ```

---

## Usage

### Main Menu
Upon running the program, you'll see the main menu:
```
### ABC NATIONAL SCHOOL ###
School Management System

1. Register New Student
2. Update Student Information
3. Add/Update Subject Mark
4. Remove Student
5. View Student Details
6. Exit System
```

Select an option by entering the corresponding number.

### Examples

#### Registering a New Student
1. Select **1** from the main menu.
2. Enter the student's ID, name, age, and grade.
3. The system will save the student's information.

#### Updating Student Information
1. Select **2** from the main menu.
2. Enter the student's ID.
3. Update the student's name, age, or grade as needed.

#### Adding/Updating Marks
1. Select **3** from the main menu.
2. Choose either:
   - **1** to add marks for a student.
   - **2** to update an existing student's marks.
3. Enter marks for the subjects (Mathematics, Science, English, Sinhala).

#### Viewing Student Details
1. Select **5** from the main menu.
2. Enter the student's ID.
3. View the student's information and their marks with grades.

#### Removing a Student
1. Select **4** from the main menu.
2. Enter the student's ID.
3. Confirm the removal of the student.

---

## Notes

- The program does not persist data across sessions. Once the program exits, all data is cleared.
- Marks must be between 0 and 100.
- Grades are calculated based on the following criteria:
  - `A+`: 90–100
  - `A`: 80–89
  - `B`: 70–79
  - `C`: 60–69
  - `F`: Below 60

---

## License

This project is licensed under the Creative Common License. Feel free to use and modify it as needed.
