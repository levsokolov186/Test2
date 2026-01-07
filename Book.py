class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "В наличии" if not self.is_borrowed else "Выдана"
        return f"'{self.title}' - {self.author} ({self.year}) ISBN: {self.isbn} [{status}]"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.isbn}')"