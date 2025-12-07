class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
    
    def __str__(self):
        return f"[{self.isbn}] {self.title} by {self.author} - ({self.status})"
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }
    
    def issue(self):
        if self.is_available():
            self.status = "issued"
            return True    
        return False
    
    def return_book(self):
        self.status = "available"
    
    def is_available(self):
        return self.status == "available"