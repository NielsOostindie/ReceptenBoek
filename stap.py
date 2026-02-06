class Stap:
    def __init__(self, beschrijving: str):
        self.__beschrijving__ = beschrijving
    
    def __str__(self):
        return self.__beschrijving__