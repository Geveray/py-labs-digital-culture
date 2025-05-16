import doctest


class Lamp:
    def __init__(self, max_brightness: float, current_brightness: float):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param max_brightness: Максимальная яркость лампы
        :param current_brightness: Текущая яркость лампы

        Примеры:
        >>> lamp = Lamp(100, 10) # инициализация экземпляра класса
        """
        if not isinstance(max_brightness, (int, float)):
            raise TypeError("Максимальная яркость лампы должна быть типа int или float")
        if max_brightness <= 0:
            raise ValueError("Максимальная яркость лампы должна быть положительным ненулевым числом.")
        self.max_brightness = max_brightness

        if not isinstance(current_brightness, (int, float)):
            raise TypeError("Текущая яркость лампы должна быть типа int или float")
        if current_brightness < 0:
            raise ValueError("Текущая яркость лампы должна быть положительным числом.")
        self.current_brightness = current_brightness

    def is_light_on(self) -> bool:
        """
        Функция, которая проверяет, включена ли лампа

        :return: Включена ли лампа

        Примеры:
        >>> lamp = Lamp(100, 1)
        >>> lamp.is_light_on()
        True
        """
        if self.current_brightness == 0:
            return False
        else:
            return True

    def set_lamp_brightness(self, brightness: float = 0) -> None:
        """
        Установка яркости лампы.
        :param brightness: Величина устанавливаемой яркости. По умолчанию лампа выключается на полную яркость

        :raise ValueError: Если величина яркости выше предела лампы

        Примеры:
        >>> lamp = Lamp(100, 10)
        >>> lamp.set_lamp_brightness(40)
        """
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость должна быть типа int или float")
        if brightness < 0:
            raise ValueError("Яркость должна быть положительным числом.")
        if brightness > self.max_brightness:
            raise ValueError("Яркость не должна превышать предела данной лампы, а именно", self.max_brightness)
        self.current_brightness = brightness


class Book_shelf:
    def __init__(self, max_books: float, current_books: list):
        """
        Создание и подготовка к работе объекта "Книжная полка"

        :param max_books: Количество книг, которое помещается на полке
        :param current_books: Название книг, стоящих на полке

        Примеры:
        >>> shelf1 = Book_shelf(5, ["Понедельник начинается в субботу", "Мы"]) # инициализация экземпляра класса
        """
        if not isinstance(max_books, (int, float)):
            raise TypeError("Количество книг, которое помещается на полке должно быть типа int или float")
        if max_books <= 0:
            raise ValueError("Количество книг, которое помещается на полке должно быть положительным ненулевым числом.")
        self.max_books = max_books

        if not isinstance(current_books, list):
            raise TypeError("Книге на полке должы быть записаны в список.")
        for book in current_books:
            if not isinstance(book, str):
                raise TypeError("Название книг на полке должны быть строками.")
        if len(current_books) > max_books:
            raise ValueError("Список книг на полке не может содержать книг больше чем может вместить полка.")
        self.current_books = current_books

    def is_shelf_empty(self) -> bool:
        """
        Функция которая проверяет является ли полка пустой

        :return: Является ли полка пустой

        Примеры:
        >>> shelf1 = Book_shelf(10, ["Понедельник начинается в субботу", "Мы"])
        >>> shelf1.is_shelf_empty()
        False
        """
        if len(self.current_books) == 0:
            return True
        else:
            return False

    def add_book_to_shelf(self, book: str) -> None:
        """
        Функция, которая добавляет книгу на полку
        :param book: Название добавляемой книги

        :raise ValueError: Если название не представленно строкой

        Примеры:
        >>> shelf1 = Book_shelf(10, ["Понедельник начинается в субботу", "Мы"])
        >>> shelf1.add_book_to_shelf("Приключения электроника")
        """
        if len(self.current_books) == self.max_books:
            ValueError("Полка заполненна, добавление не возможно.")
        if not isinstance(book, str):
            raise TypeError("Название книги должно быть представлено строкой")
        self.current_books.append(book)

    def delete_book_from_shelf(self, book_index: int = -1) -> None:
        """
        Функция по удалению n-ой книги с полки
        :param book_index: Номер книги слева на право, начиная с 1

        :raise ValueError: номер не должен превышать количество книг на полке в данный момент.

        Примеры:
        >>> shelf1 = Book_shelf(10, ["Понедельник начинается в субботу", "Мы"])
        >>> shelf1.delete_book_from_shelf(2)
        """
        if not isinstance(book_index, int):
            raise TypeError("Номер должен быть целым числом.")
        if book_index < 1:
            raise ValueError("Номерация книг начинается с 1")
        if book_index > len(self.current_books):
            raise ValueError("Можно убрать только те книги, которые стоят на полке, пока что их", len(self.current_books))
        self.current_books.pop(book_index-1)


class Boudget:
    def __init__(self, podushka: float, subscriptions: float):
        """
        Создание и подготовка к работе объекта "Бюджет"

        :param podushka: Скопленные к данному моменту деньги
        :param subscriptions: Ежемесячное списывание за подписки на сервисы

        Примеры:
        >>> boudget1 = Boudget(5000, 350) # инициализация экземпляра класса
        """
        if not isinstance(podushka, (int, float)):
            raise TypeError("Бюджет должен выражаться числом.")
        if podushka < 0:
            raise ValueError("Бюджет не должен изначально быть отрицательным.")
        self.boudget = podushka

        if not isinstance(subscriptions, (int, float)):
            raise TypeError("Плата за подписки выражается числом.")
        if subscriptions < 0:
            raise ValueError("Плата за подписки не должна быть отрицательной.")
        self.subscriptions = subscriptions

    def new_month(self, salary: float = 0, spend: float = 0) -> float:
        """
        Функция рассчёта бюджета в новом месяце, с учётом всех доходов и расходов.
        :param salary: Зарплата
        :param spend: Деньги, что мы потратили (без учёта подписок)

        :return: Бюджет в новом месяце

        :raise ValueError: Условия не должны приводить к нашему банкротству.

        Примеры:
        >>> boudget1 = Boudget(5000, 200)
        >>> boudget1.new_month(1000, 500)
        5300
        """
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата должна выражаться числом")
        if not isinstance(spend, (int, float)):
            raise TypeError("Потраченные деньги должны выражаться числом")
        if salary < 0 or spend < 0:
            raise ValueError("И зарплата, и потраченные деньги должны быть положительными числами.")
        new_boudget = round(self.boudget - self.subscriptions + salary - spend, 2)
        if new_boudget < 0:
            raise ValueError("При таких условиях мы обанкротимся.")
        self.boudget = new_boudget
        return new_boudget

    def set_subscriptions(self, new_sub: float) -> None:
        """
        Функция которая позволит установить, сколько с нас списывается за подписки
        :param new_sub: Новая стоимость подписок

        :raise ValueError: Не допускается брать подписки превышающие нынешний бюджет

        Примеры:
        >>> boudget1 = Boudget(5000, 200)
        >>> boudget1.set_subscriptions(300)
        """
        if not isinstance(new_sub, (int, float)):
            raise TypeError("Стоимость подписок должна выражаться числом.")
        if new_sub < 0:
            raise ValueError("Стоимость подписок не может быть отрицательной")
        if new_sub > self.boudget:
            raise ValueError("Не допускается брать подписки превышающие нынешний бюджет. Он составляет", self.boudget)
        self.subscriptions = new_sub


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации