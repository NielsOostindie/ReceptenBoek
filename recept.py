from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen_list = []
        self.__aantal_personen: int = 1

    def __str__(self):
        return self.__naam

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list

    def get_naam(self) -> str:
        return self.__naam

    def get_omschrijving(self) -> str:
        return self.__omschrijving

    def voeg_stap_toe(self, stap: Stap):
        self.__stappen_list.append(stap)

    def get_stappen(self):
        return self.__stappen_list

    def set_aantal_personen(self, personen: int):
        factor = personen / self.__aantal_personen
        for ingredient in self.__ingredient_list:
            ingredient.set_hoeveelheid(ingredient.get_hoeveelheid() * factor)
        self.__aantal_personen = personen

    def get_aantal_personen(self) -> int:
        return self.__aantal_personen

    def get_plantaardig_recept(self, plantaardig: bool):
        """Geeft de ingrediënten terug, eventueel vervangen door plantaardige alternatieven."""
        return [ing.get_ingredient(plantaardig) for ing in self.__ingredient_list]

    def get_totaal_kcal(self, plantaardig: bool = False) -> int:
        ingredienten = self.get_plantaardig_recept(plantaardig)
        return sum(ing.get_kcal() for ing in ingredienten)

    def toon_recept(self, plantaardig: bool = False):
        print(f"\n{'=' * 50}")
        print(f"Recept: {self.__naam}")
        print(f"Omschrijving: {self.__omschrijving}")
        print(f"Personen: {self.__aantal_personen}")
        print(f"\nIngrediënten:")
        for ing in self.get_plantaardig_recept(plantaardig):
            print(f"  • {ing}")
        print(f"\nBereidingsstappen:")
        for i, stap in enumerate(self.__stappen_list, 1):
            print(f"  {i}. {stap}")
        print(f"\nTotaal kcal: {self.get_totaal_kcal(plantaardig)} kcal")
        print(f"{'=' * 50}")