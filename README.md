# Student Database Management System

A Python-based project to manage student data, integrated with a MySQL database.
This application uses a Tkinter GUI for the user interface.

## Steps to Run the Project

1. **Create a Database in MySQL**
   - Open your MySQL client or GUI (MySQL Workbench or MySql cmd line).
   - Create a database:
     ```sql
     CREATE DATABASE your_database_name;
     ```
   - Replace `your_database_name` with the name of your database in the Python code.

2. **Update the Database Credentials**
   - Open the Python code file (`main.py`).
   - Locate the section where the database connection is defined (e.g., using `mysql.connector` or `SQLAlchemy`).
   - Update the following fields:
     ```python
     db_name = "your_database_name"
     user = "your_username"
     password = "your_password"
     host = "localhost"  # or your database host
     ```
     Replace `your_username` and `your_password` with your MySQL credentials.

3. **Install Dependencies**
   - Ensure Python is installed on your system.
   - Install required dependencies using `pip`:
     ```bash
     pip install mysql-connector-python
     ```

4. **Run the Application**
   - Start the application:
     ```bash
     python main.py
     ```

5. **Access the Application**
   - Open the application interface or test the backend functionality as described in  project.

---

## Features
- Add, update, and delete student records.
- Query student information from the database.
- User-friendly interface with database integration.

---

## Requirements
- Python 3.x
- MySQL
- Required Python libraries (listed in `requirements.txt`)

---

## Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes.

---
## Output
![output](https://github.com/user-attachments/assets/650e7aff-266d-44ce-9138-6f7de1b408f8)

