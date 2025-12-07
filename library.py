"""
Name: Prithvee Singh Yadav
Roll no: 2501010087
Title: Library Inventory Manager
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manager.inventory import LibraryInventory

def print_menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search by Title")
    print("5. View All Books")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        print_menu()
        choice = input("Enter choice: ")

        # Task 5: Exception Handling for Input
        try:
            if choice == '1':
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                if title and author and isbn:
                    inventory.add_book(title, author, isbn)
                else:
                    print("Error: All fields are required.")

            elif choice == '2':
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book:
                    if book.issue():
                        inventory.save_books()
                        print(f"Book '{book.title}' issued successfully.")
                    else:
                        print("Error: Book is already issued.")
                else:
                    print("Error: Book not found.")

            elif choice == '3':
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book:
                    book.return_book()
                    inventory.save_books()
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print("Error: Book not found.")

            elif choice == '4':
                query = input("Enter title to search: ")
                results = inventory.search_by_title(query)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No matching books found.")

            elif choice == '5':
                inventory.display_all()

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()