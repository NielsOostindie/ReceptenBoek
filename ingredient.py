class Ingredient:

    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
   
    def __str__(self):
        return f"{self.__naam} - {self.__hoeveelheid} {self.__eenheid}"