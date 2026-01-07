class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id
        self.borrowed_books = []

    def __str__(self):
        books_count = len(self.borrowed_books)
        return f"{self.name} (ID: {self.person_id}), книг на руках: {books_count}"

    def __repr__(self):
        return f"Person('{self.name}', '{self.person_id}')"

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return True
        return False