
Student Data Management System

Overview

The Student Data Management System is a Tkinter-based application designed to manage student information efficiently. It allows users to add, update, delete, and view student records. The application uses an SQLite database to store student data and provides a graphical user interface (GUI) to interact with the data.

## Features

- **Add Student**: Input and save new student details into the database.
- **Update Student**: Modify existing student records.
- **Delete Student**: Remove student records from the database.
- **View All Students**: Display all student records in a tabular format.
- **Clear Form**: Reset the input fields to their default state.

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Ensure you have `tkinter` and `sqlite3` libraries available (or) pip install --tkinter, pip install --sqlite3. These are usually included with Python. No additional packages are required.

## Usage

1. **Run the Application**

   Ensure you have Python installed, then run the `main.py` file:

   ```bash
   python main.py
   ```

2. **Using the Application**

   - **Entries Frame**: Input student details in the provided fields.
   - **Buttons**: Use the buttons to add, update, delete, or clear records.
   - **Table**: View all student records in the table below the input fields. Click on a record in the table to populate the input fields for updating or deleting.

## Database Schema

The application uses an SQLite database (`student.db`) with the following table schema:

- **students**:
  - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
  - `name` (TEXT)
  - `dob` (DATE)
  - `gender` (TEXT)
  - `email` (TEXT)
  - `phone` (TEXT)
  - `address` (TEXT)
  - `enrolment_no` (TEXT)
  - `grade` (TEXT)

## Code Structure

- **`main.py`**: Main application code, containing the Tkinter GUI and logic for interacting with the database.
- **`db.py`**: Database handling code, including methods for CRUD (Create, Read, Update, Delete) operations.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Name**: Kalainidhi S
- **Email**: kalainidhias001@gmail

