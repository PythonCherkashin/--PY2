class Cats:
    """"Класс, описывающий котов"""
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Кошку зовут {self.name}. Ей {self.age}.'
        """ Данный метод описывает самые базовые характеристики любой кошки - ее имя и возраст.  """

class Savannah(Cats):
    """ Дочерний класс, описывающий породу 'Саванна'"""
    def __init__(self, name: str, age: int, height: int, weight: int) :
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return f'Саванна зовут {self.name}. Ей {self.age}. Рост Саванна - {self.height}. Вес Саванна - {self.weight}.'
        """Данный метод описывает базовые характеристики 'Саванна'. 
        Перегрузка этого метода необходима, чтобы указать рост и вес. """

if __name__ == "__main__":
    # Write your solution here
    pass