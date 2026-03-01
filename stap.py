class Stap:
    def __init__(self, beschrijving: str, tip: str = None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def __str__(self):
        tekst = self.__beschrijving
        if self.__tip:
            tekst += f"\n   💡 Tip: {self.__tip}"
        return tekst

    def get_beschrijving(self) -> str:
        return self.__beschrijving

    def get_tip(self) -> str:
        return self.__tip

    def set_tip(self, tip: str):
        self.__tip = tip