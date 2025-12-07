from pathlib import Path
from .book import Book
import json
import logging

class LibraryInventory:
    def __init__(self, filename="library.json"):
        # Always save/load JSON from the same folder as inventory.py
        base_dir = Path(__file__).resolve().parent
        self.file_path = base_dir / filename

        self.books = []
        self.load_books()