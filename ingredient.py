class Ingredient:

    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, altenatief: str = None, kcal: float = None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__plantaardig = altenatief
        self.__eenheid = eenheid
        self.__kcal = kcal
   
    def __str__(self, toon_alternatief=True):
        if self.__plantaardig is not None and toon_alternatief:
            plantaardig_str = f" (of {self.__plantaardig})"
        else:            plantaardig_str = ""
        kcal_str = f" ({self.__kcal} kcal)" if self.__kcal is not None else ""
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}{plantaardig_str}{kcal_str}"
    
    def get_kcal(self):
        return self.__kcal
    
    def get_alternatief(self):
        return self.__plantaardig