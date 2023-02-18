class Swimming:
    """
    Этот класс описывает модель бассейна.
    """
    def __init__(self):
        self.heats = 5
        self.swimmers = 10

    def pump_swimming(self, done_heats) -> int:
        """
        Метод увеличивает количество сделанных заплывов
        :return: Количество сделанных заплывов

        """
        if not isinstance(done_heats, int):
            raise TypeError("Количество заплывов должно быть типа int")
        if done_heats < 0:
            raise ValueError("Количество заплывов не может быть меньше 0")

        self.heats += done_heats

    def amount_of_swimmers(self) -> int:
        """
        Метод, считающий пловцов в бассейне
        :return: Количество пловцов в бассейне на данный момент

        """
        ...



class YouTube:
    """
    Данный класс описывает модель ютуба
    """
    def __init__(self):
        self.followers = 200
        self.subscriptions = 100

    def followers_increase(self, amount_of_followers) -> int:
        """
        Метод увеличивает число подписчиков
        :return: показывает текущее количество подписчиков

        """
        if not isinstance(amount_of_followers,int):
            raise TypeError("Количество подписчиков должно быть типа int")
        ...

    def subscriptions_increase(self, amount_of_subscriptions) -> int:
        """
         Метод увеличивает число подписок
        :return: показывает текущее аоличество подписок
        """
        if not isinstance(amount_of_subscriptions, int):
            raise TypeError("Количество подписок должно быть типа int")
        ...

class Restaurant:
    """
Данный метод описывает модель свободных столиков в ресторане

    """
    def __init__(self):
        self.people = 50
        self.vacant_tables = 100

    def is_place_tables(self)-> bool:
        """
        Метод показывает, занят ли столик
        :return: Занят ли столик

        """
        ...
    def vacant_tables_amount(self) -> int:
        """
        Метод показывает остаток свободных столиков в ресторане
        :return: Количество свободных столиков в ресторане
        """
        ...
if __name__  == "__main__":
    import doctest
    doctest.testmod()