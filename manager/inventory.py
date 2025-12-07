import json
import logging
from pathlib import Path
from .book import Book

# Task 5: Setup Logging (Basic config)
logging.basicConfig(
    filename='library.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LibraryInventory:
    def __init__(self, filename="library.json"):
        self.file_path = Path(filename)
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn):
        # Check for duplicate ISBN
        if self.search_by_isbn(isbn):
            logging.warning(f"Attempted to add duplicate ISBN: {isbn}")
            print("Error: A book with this ISBN already exists.")
            return
        
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        logging.info(f"Book added: {title} ({isbn})")
        print("Book added successfully.")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
        for book in self.books:
            print(book)

    # Task 3: File Persistence
    def save_books(self):
        try:
            # Convert all Book objects to dictionaries
            data = [book.to_dict() for book in self.books]
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logging.error(f"Failed to save data: {e}")
            print("Error saving database.")

    def load_books(self):
        if not self.file_path.exists():
            logging.info("No database found. Creating new inventory.")
            return

        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                # Convert list of dicts back to list of Book objects
                self.books = [Book(**item) for item in data]
            logging.info("Database loaded successfully.")
        except json.JSONDecodeError:
            logging.error("Database file corrupted.")
            print("Error: Database file is corrupted.")
        except Exception as e:
            logging.error(f"Error loading database: {e}")