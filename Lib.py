class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.people = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Книга '{book.title}' добавлена в библиотеку")
        else:
            print("Эта книга уже есть в библиотеке")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print(f"Нельзя удалить книгу '{book.title}', так как она выдана читателю")
                    return False
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из библиотеки")
                return True
        print("Книга с таким ISBN не найдена")
        return False

    def find_book(self, search_term):
        results = []
        search_term = search_term.lower()
        for book in self.books:
            if (search_term in book.title.lower() or
                    search_term in book.author.lower() or
                    search_term in book.isbn):
                results.append(book)
        return results

    def add_person(self, person):
        if person not in self.people:
            self.people.append(person)
            print(f"Читатель {person.name} добавлен")
        else:
            print("Этот читатель уже зарегистрирован")

    def remove_person(self, person_id):
        for person in self.people:
            if person.person_id == person_id:
                if person.borrowed_books:
                    print(f"Нельзя удалить читателя {person.name}, так как у него есть книги на руках")
                    return False
                self.people.remove(person)
                print(f"Читатель {person.name} удален")
                return True
        print("Читатель с таким ID не найден")
        return False

    def find_person(self, search_term):
        results = []
        search_term = search_term.lower()
        for person in self.people:
            if (search_term in person.name.lower() or
                    search_term in person.person_id):
                results.append(person)
        return results

    def borrow_book_to_person(self, isbn, person_id):
        book = None
        person = None

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        for p in self.people:
            if p.person_id == person_id:
                person = p
                break

        if not book:
            print("Книга не найдена")
            return False

        if not person:
            print("Читатель не найден")
            return False

        if person.borrow_book(book):
            print(f"Книга '{book.title}' выдана читателю {person.name}")
            return True
        else:
            print(f"Книга '{book.title}' уже выдана другому читателю")
            return False

    def return_book_from_person(self, isbn, person_id):
        book = None
        person = None

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        for p in self.people:
            if p.person_id == person_id:
                person = p
                break

        if not book or not person:
            print("Книга или читатель не найдены")
            return False

        if person.return_book(book):
            print(f"Книга '{book.title}' возвращена читателем {person.name}")
            return True
        else:
            print(f"У читателя {person.name} нет этой книги")
            return False

    def list_books(self):
        print(f"\nКниги в библиотеке '{self.name}' (всего: {len(self.books)}):")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def list_people(self):
        print(f"\nЧитатели библиотеки '{self.name}' (всего: {len(self.people)}):")
        for i, person in enumerate(self.people, 1):
            print(f"{i}. {person}")
            if person.borrowed_books:
                print("   На руках:")
                for j, book in enumerate(person.borrowed_books, 1):
                    print(f"   {j}. {book.title}")

    def get_statistics(self):
        total_books = len(self.books)
        borrowed_books = sum(1 for book in self.books if book.is_borrowed)
        total_people = len(self.people)

        print(f"\nСтатистика библиотеки '{self.name}':")
        print(f"Всего книг: {total_books}")
        print(f"Книг выдано: {borrowed_books}")
        print(f"Книг в наличии: {total_books - borrowed_books}")
        print(f"Зарегистрировано читателей: {total_people}")