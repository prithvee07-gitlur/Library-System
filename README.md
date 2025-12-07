# Library Inventory Manager

A simple command-line interface (CLI) application developed in Python to manage a library's book inventory. This system allows users to add, search, issue, and return books, ensuring data is saved persistently.

## 📋 Features

* **Add Books:** Input details like Title, Author, and ISBN to add new books to the inventory.
* **Issue & Return:** Manage book circulation by changing the status of books between "available" and "issued".
* **Search:** Find books quickly by searching for their titles.
* **View Inventory:** Display a list of all books currently in the system.
* **Data Persistence:** All data is automatically saved to `library.json`, so records are not lost when the program closes.
* **Logging:** Tracks system events (like loading the database or adding books) in `library.log`.

## 📂 Project Structure

* **library.py:** Main application script (Entry point).
* **library.json:** Data storage file.
* **library.log:** Activity log file.
* **manager/:** Package containing business logic.
  * **\_\_init\_\_.py:** Initializes the package and handles LibraryInventory.
  * **book.py:** Defines the Book class and properties.

## 🚀 How to Run

* **Prerequisites:** Ensure you have Python 3.x installed on your system.
* **Setup:** Place the `library.py` file and the `manager` folder (containing `__init__.py` and `book.py`) in the same directory.
* **Execution:** Open your terminal in the project folder and run the command `python library.py`.

## 🛠️ Usage

Once the program is running, follow the on-screen menu:

1.  **Add Book:** Enter option `1` and provide the required details.
2.  **Issue Book:** Enter option `2` and the ISBN of the book to issue.
3.  **Return Book:** Enter option `3` and the ISBN of the book to return.
4.  **Search:** Enter option `4` to find a specific book by title.
5.  **View All:** Enter option `5` to see the full list of books.
6.  **Exit:** Enter option `6` to close the application.

## 👤 Author

**Prithvee Singh Yadav**
* **Roll No:** 2501010087
* **Project:** Library Inventory Manager
