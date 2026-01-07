from book import Book
from person import Person
from library import Library


def create_sample_data(library):
    """Создание тестовых данных"""
    # Добавляем книги
    books_data = [
        ("Война и мир", "Лев Толстой", 1869, "978-5-389-07435-1"),
        ("Преступление и наказание", "Федор Достоевский", 1866, "978-5-699-06615-4"),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5-17-067842-4"),
        ("1984", "Джордж Оруэлл", 1949, "978-5-17-090640-4"),
        ("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "978-5-389-07464-1")
    ]

    for title, author, year, isbn in books_data:
        library.add_book(Book(title, author, year, isbn))

    # Добавляем читателей
    people_data = [
        ("Иван Иванов", "001"),
        ("Петр Петров", "002"),
        ("Мария Сидорова", "003")
    ]

    for name, person_id in people_data:
        library.add_person(Person(name, person_id))


def main():
    # Создаем библиотеку
    library = Library("Центральная городская библиотека")

    # Добавляем тестовые данные
    create_sample_data(library)

    while True:
        print("\n" + "=" * 50)
        print("БИБЛИОТЕЧНАЯ СИСТЕМА")
        print("=" * 50)
        print("1. Управление книгами")
        print("2. Управление читателями")
        print("3. Выдача/возврат книг")
        print("4. Показать все книги")
        print("5. Показать всех читателей")
        print("6. Поиск книг")
        print("7. Поиск читателей")
        print("8. Статистика")
        print("9. Выйти")
        print("=" * 50)

        choice = input("Выберите действие (1-9): ")

        if choice == "1":
            print("\nУПРАВЛЕНИЕ КНИГАМИ")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Назад")

            sub_choice = input("Выберите действие: ")

            if sub_choice == "1":
                print("\nДОБАВЛЕНИЕ НОВОЙ КНИГИ")
                title = input("Название: ")
                author = input("Автор: ")
                year = input("Год издания: ")
                isbn = input("ISBN: ")

                try:
                    year = int(year)
                    new_book = Book(title, author, year, isbn)
                    library.add_book(new_book)
                except ValueError:
                    print("Ошибка: год должен быть числом")

            elif sub_choice == "2":
                print("\nУДАЛЕНИЕ КНИГИ")
                isbn = input("Введите ISBN книги для удаления: ")
                library.remove_book(isbn)

        elif choice == "2":
            print("\nУПРАВЛЕНИЕ ЧИТАТЕЛЯМИ")
            print("1. Добавить читателя")
            print("2. Удалить читателя")
            print("3. Назад")

            sub_choice = input("Выберите действие: ")

            if sub_choice == "1":
                print("\nДОБАВЛЕНИЕ НОВОГО ЧИТАТЕЛЯ")
                name = input("ФИО: ")
                person_id = input("ID читателя: ")

                new_person = Person(name, person_id)
                library.add_person(new_person)

            elif sub_choice == "2":
                print("\nУДАЛЕНИЕ ЧИТАТЕЛЯ")
                person_id = input("Введите ID читателя для удаления: ")
                library.remove_person(person_id)

        elif choice == "3":
            print("\nВЫДАЧА/ВОЗВРАТ КНИГ")
            print("1. Выдать книгу")
            print("2. Вернуть книгу")
            print("3. Назад")

            sub_choice = input("Выберите действие: ")

            if sub_choice == "1":
                print("\nВЫДАЧА КНИГИ")
                isbn = input("ISBN книги: ")
                person_id = input("ID читателя: ")
                library.borrow_book_to_person(isbn, person_id)

            elif sub_choice == "2":
                print("\nВОЗВРАТ КНИГИ")
                isbn = input("ISBN книги: ")
                person_id = input("ID читателя: ")
                library.return_book_from_person(isbn, person_id)

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            library.list_people()

        elif choice == "6":
            print("\nПОИСК КНИГ")
            search_term = input("Введите название, автора или ISBN: ")
            results = library.find_book(search_term)

            if results:
                print(f"\nНайдено {len(results)} книг:")
                for i, book in enumerate(results, 1):
                    print(f"{i}. {book}")
            else:
                print("Книги не найдены")

        elif choice == "7":
            print("\nПОИСК ЧИТАТЕЛЕЙ")
            search_term = input("Введите ФИО или ID: ")
            results = library.find_person(search_term)

            if results:
                print(f"\nНайдено {len(results)} читателей:")
                for i, person in enumerate(results, 1):
                    print(f"{i}. {person}")
            else:
                print("Читатели не найдены")

        elif choice == "8":
            library.get_statistics()

        elif choice == "9":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()