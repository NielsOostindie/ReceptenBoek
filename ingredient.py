class Ingredient:

    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal: int = 0):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = None

    def __str__(self):
        return f"{self.__naam} - {self.__hoeveelheid} {self.__eenheid} ({self.__kcal} kcal)"

    def set_hoeveelheid(self, hoeveelheid: float):
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self) -> float:
        return self.__hoeveelheid

    def get_kcal(self) -> int:
        return self.__kcal

    def set_plantaardig_alternatief(self, alternatief: 'Ingredient'):
        self.__plantaardig_alternatief = alternatief

    def get_ingredient(self, plantaardig: bool) -> 'Ingredient':
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        return self

    def get_naam(self) -> str:
        return self.__naam

    def get_eenheid(self) -> str:
        return self.__eenheid

    def heeft_plantaardig_alternatief(self) -> bool:
        return self.__plantaardig_alternatief is not None