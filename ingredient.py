class Ingredient:

    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self.__naam__ = naam
        self.__hoeveelheid__ = hoeveelheid
        self.__eenheid__ = eenheid

    def __str__(self):
        return f"{self.__hoeveelheid__} {self.__eenheid__} {self.__naam__}"