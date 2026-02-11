from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram"))

    recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even)."))

    recepten.append(recept1)

    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")
    recept2.voeg_ingredient_toe(Ingredient("gehakt", 500, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 2, "stuks"))
    recept2.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden."))
    recept2.voeg_stap_toe(Stap("Bak het gehakt rul in een pan en voeg de gesneden paprika toe."))

    recepten.append(recept2)

    recept3 = Recept("Pasta Carbonara", "Een klassieke Italiaanse pasta met spek en kaas.")
    recept3.voeg_ingredient_toe(Ingredient("pasta", 400, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("spek", 200, "gram"))
    recept3.voeg_stap_toe(Stap("Kook de pasta volgens de aanwijzingen op de verpakking."))
    recept3.voeg_stap_toe(Stap("Bak het spek krokant in een pan."))

    recepten.append(recept3)
    
    for recept in recepten:
        print(f"hoeveel personen wil je: {recept._Recept__naam} maken?")
        aantal_personen = int(input())
        recept.schaal_recept(aantal_personen)
        print(f"Recept: {recept._Recept__naam}")
        print(f"Omschrijving: {recept._Recept__omschrijving}")
        print("Ingrediënten:")
        for ingredient in recept._Recept__ingredient_list:
            print(f"  - {ingredient}")
        print()

if __name__ == "__main__":
    main()
