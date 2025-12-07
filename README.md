# Library-System
📚 Library Inventory Manager
A project by Prithvee Singh Yadav (Roll No: 2501010087)

This is a console-based Library Management System built in Python.
It allows users to add books, issue books, return them, search the library, and view all books.
Book data is stored persistently in library.json, ensuring that changes remain saved even after the program is closed.

🚀 Features
1. Add Books
Enter Title, Author, and ISBN
Prevents duplicate ISBN entries
Automatically saves to library.json
2. Issue a Book
Issues a book by its ISBN
Prevents issuing a book already marked as issued
3. Return a Book
Returns a previously issued book
Updates the status back to available
4. Search by Title
Case-insensitive search
Returns a list of matching books
5. View All Books
Displays all books in a clean readable format
Shows: ISBN, Title, Author, Status
6. JSON File Persistence
All books are stored in:

manager/library.json
The system automatically loads and saves data using LibraryInventory.save_books() and load_books().

📁 Project Structure
Library-inventory/
 Library.py               # Main program entry point
manager/
│   ├── __init__.py
│   ├── book.py               # Book class (title, author, isbn, status)
│   ├── inventory.py          # LibraryInventory class + JSON handling
│   └── library.json          # Persistent database of books
🧠 How It Works
Book Class
Located in library_manager/book.py

Represents a single book
Contains methods:
issue()
return_book()
is_available()
to_dict() → used for JSON conversion
LibraryInventory Class
Located in library_manager/inventory.py

Loads books at startup
Adds, issues, returns, searches, and displays books
Saves books automatically to JSON
Uses:
from pathlib import Path
base_dir = Path(__file__).resolve().parent
self.file_path = base_dir / "library.json"
This ensures JSON is always stored correctly in library_manager/.

Main Application
Located in cli/main.py

Shows menu options
Routes user input to LibraryInventory methods
Handles basic input validation
🧪 Unit Testing
Tests are included for the Book class:

tests/tests.py
Run tests using:

python -m unittest tests/tests.py
Tests verify:

Book creation
Initial status
Issuing / returning behavior
▶️ Running the Application
Step 1: Navigate to the project folder
cd Library-inventory
Step 2: Run the main script
python cli/main.py
Step 3: Use the menu
1. Add Book
2. Issue Book
3. Return Book
4. Search by Title
5. View All Books
6. Exit
📌 Notes
JSON is automatically created if it does not exist
A log file library.log is generated for warnings/errors
The application gracefully handles invalid inputs using exception handling
