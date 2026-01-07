import Book
import People

bookOne = 'Лев Толстой'
bookTwo = 'C++'

peopleOne = 'Лев'
peopleTwo = 'Женя'

listBook = ()
listPeople = ()

Book.CreateBook(bookOne, listBook)
Book.CreateBook(peopleOne, listPeople)
People.CreatePeople(bookTwo, listBook)
People.DeletePeople(peopleTwo, listPeople)

Book.DeleteBook(bookOne, listBook)
People.DeletePeople(peopleOne, listPeople)