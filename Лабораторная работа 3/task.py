class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом!")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным ненулевым числом.")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self._pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность должна выражаться числом.")
        if duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным ненулевым числом.")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self._duration})"
