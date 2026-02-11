class Stap:
    def __init__(self, beschrijving: str, tip: str = None):
        self.__beschrijving__ = beschrijving
        self.__tip__ = tip

    def __str__(self):
        if self.__tip__:
            return f"{self.__beschrijving__} (Tip: {self.__tip__})"
        else:
            return self.__beschrijving__