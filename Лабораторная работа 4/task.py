class Lamp:
    def __init__(self, max_brightness: float, current_brightness: float):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param max_brightness: Максимальная яркость лампы. Это её характеристика, в работе меняться не будет, потому мы
                    её защитим и свойством сделаем только для чтения.
        :param current_brightness: Текущая яркость лампы.

        Примеры:
        >>> lamp = Lamp(100, 10) # инициализация экземпляра класса
        """
        if not isinstance(max_brightness, (int, float)):
            raise TypeError("Максимальная яркость лампы должна быть типа int или float")
        if max_brightness <= 0:
            raise ValueError("Максимальная яркость лампы должна быть положительным ненулевым числом.")
        self._max_brightness = max_brightness
        self.current_brightness = current_brightness
        self.voltage = []

    @property
    def max_brightness(self):
        return self._max_brightness

    @property
    def current_brightness(self):
        return self._current_brightness

    @current_brightness.setter
    def current_brightness(self, current_brightness):
        if not isinstance(current_brightness, (int, float)):
            raise TypeError("Яркость лампы должна быть типа int или float")
        if current_brightness < 0:
            raise ValueError("Яркость лампы не должна быть отрицательным числом.")
        self._current_brightness = current_brightness


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
        :param brightness: Величина устанавливаемой яркости. По умолчанию лампа выключается

        :raise ValueError: Если величина яркости выше предела лампы
        :raise TypeError: Если яркость передана не числовым форматом
        :raise ValueError: Если яркость устанавляивается отрицательной

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

    def __str__(self) -> str:
        return f"Лампа с яркостью {self.current_brightness}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(max_brightness={self.max_brightness}, ' \
               f'current_brightness={self.current_brightness})'

class Diode_lamp(Lamp):
    """
    Создание и подготовка к работе дочернего (для класса "Лампа") класса "Светодиодная лампа"
    Кроме унаследованных от класса "Лампа" атрибутов max_brightness и current_parameters, этот класс имеет уникальный атрибут
    :param colour: Цвет светодиодной лампы

    Из базового класса мы наследуем методы установки яркости и проверки на вкл/выкл


    :raise TypeError: Если цввете передан не строкой
    :raise ValueError: Если цвет не соответствует списку разрешённых цветов.

    Пример:
    >>> d_lamp1 = Diode_lamp(100, 10, "red")
    """
    def __init__(self, max_brightness: float, current_brightness: float, colour: str) -> None:
        # Используем инициализатор класса выше для унаследованных параметров.
        super().__init__(max_brightness, current_brightness)

        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть представлен строкой")
        if not (colour in ("red", "green", "blue", "orange", "purple")):
            raise ValueError("Цвет может быть только из списка:", ("red", "green", "blue", "orange", "purple"))
        self.colour = colour

    """
    Перегружены магические метода str и repr, в угоду добавлению информации о цвете объекта.
    """
    def __str__(self) -> str:
        return f"Лампа с яркостью {self.current_brightness} цвета {self.colour}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(max_brightness={self.max_brightness}, ' \
               f'current_brightness={self.current_brightness}, colour={self.colour})'

    def __eq__(self, other):
        """
        Перегрузка проверки равенства необходима для установки лампочек одинаковых цветов
        Пример:
        >>> diode1 = Diode_lamp(100, 20, "red")
        >>> diode2 = Diode_lamp(200, 34, "red")
        >>> diode1 == diode2 # Обе лампы красного цвета
        True
        """
        return self.colour == other.colour




lamp1 = Lamp(100,20)
lamp1.current_brightness = 150