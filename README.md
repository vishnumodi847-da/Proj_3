📚 Student Data Organizer

A simple Python CLI (Command Line Interface) project to manage student records.
This project allows you to add, display, update, delete students, and also view all subjects offered.

🚀 Features
➕ Add new student
📋 Display all students
✏️ Update student information
❌ Delete student record
📖 Display all subjects offered
🔁 Menu-driven program (easy to use)
🛠️ Technologies Used
Python 3
Basic concepts:
Lists
Dictionaries
Sets
Loops
Functions
User Input
📂 Project Structure
Proj_3.py   # Main Python file
README.md   # Project documentation
▶️ How to Run
Install Python (if not installed)

Download or clone this repository:

git clone https://github.com/your-username/student-data-organizer.git

Navigate to folder:

cd student-data-organizer

Run the program:

python Proj_3.py
📌 Menu Options

When you run the program, you will see:

1. Add Student
2. Display All Student
3. Update Student Information
4. Delete Student
5. Display Student Offered
6. Exit
🧑‍🎓 Student Data Fields

Each student contains:

Name
ID
Age
Grade
Date of Birth (DOB)
Subjects (multiple allowed)
🧠 How It Works
Student data is stored in a list of dictionaries
Each student is saved using their ID as key
Subjects are stored using a set to avoid duplicates

Example structure:

{
  student_data: {
    "name": "Vishnu",
    "age": 20,
    "grade": "A",
    "dob": "2005-01-01",
    "subjects": {"Math", "Science"}
  }
}
⚠️ Limitations
Data is not saved permanently (lost after program exit)
No file/database storage
Input validation is basic
🔧 Future Improvements
💾 Save data in file (JSON / CSV)
🖥️ Add GUI (Tkinter)
🔍 Search student by ID or name
✅ Better validation
📊 Add statistics (average age, etc.)
🐞 Known Issues
Typo in menu text (e.g., "organizar", "Updqate")
Subject update may not work correctly (key mismatch: subject vs subjects)
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch
Make changes
Submit a pull request
📜 License

This project is free to use for learning purposes.

👨‍💻 Author
Vishnu Modi
