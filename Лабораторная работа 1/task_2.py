from task_1 import Lamp, Book_shelf, Boudget


if __name__ == "__main__":
    lamp1 = Lamp(1000, 500)
    shelf1 = Book_shelf(6, ["Война миров"])
    boudget1 = Boudget(10000, 300)

    try:
     lamp1.set_lamp_brightness("600")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     shelf1.add_book_to_shelf(1984)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        boudget1.set_subscriptions("Сто три")
    except TypeError:
        print('Ошибка: неправильные данные')
