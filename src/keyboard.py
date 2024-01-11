from src.item import Item

class Changing_languages():
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, Changing_languages):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        Changing_languages.__init__(self)
