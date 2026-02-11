class Recept:
    def __init__(self, naam, omschrijving, personen=1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__personen = personen
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)
    
    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)
    
    def schaal_recept(self, aantal_personen):
        factor = aantal_personen / self.__personen
        for ingredient in self.__ingredient_list:
            ingredient._Ingredient__hoeveelheid *= factor
    
    def bereken_totaal_kcal(self):
        totaal_kcal = 0
        for ingredient in self.__ingredient_list:
            kcal = ingredient.get_kcal()
            if kcal is not None:
                totaal_kcal += kcal
        return totaal_kcal