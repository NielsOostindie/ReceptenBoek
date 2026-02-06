class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)
    
    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)