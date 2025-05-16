BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги обязан быть целочисленным")
        if id_ < 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть представленно строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Число страниц должно быть целым ненулевым числом.")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books: list = []):
        if not isinstance(books, list):
            raise TypeError("Книги должны быть представленны списком")
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self,look_id):
        if not isinstance(look_id, int):
            raise TypeError("Индекс книги должен быть целым числом")
        if look_id < 0:
            raise ValueError("Индексирование книг начинается с 1")
        for i in range(len(self.books)):
            if self.books[i].id_ == look_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
