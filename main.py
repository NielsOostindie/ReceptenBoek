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

    recept2.voeg_ingredient_toe(Ingredient("gehakt", 300, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 200, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("room", 100, "ml"))

    recept2.voeg_stap_toe(Stap("Verwarm de oven op 180 graden."))
    recept2.voeg_stap_toe(Stap("Snijd de paprika in kleine blokjes en laat ze in een pan met wat olie pruttelen."))
    recept2.voeg_stap_toe(Stap("Voeg het gehakt toe aan de paprika en bak het rul."))
    recept2.voeg_stap_toe(Stap("Meng het gehakt en de paprika met de room en giet het mengsel in een quichevorm."))
    recept2.voeg_stap_toe(Stap("Bak de quiche in de oven voor ongeveer 30 minuten, of tot de bovenkant goudbruin is."))

    recept3 = Recept("Pasta Carbonara", "Een klassieke Italiaanse pasta met een romige saus van eieren, kaas en spek.")
    recept3.voeg_ingredient_toe(Ingredient("pasta", 250, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("spek", 150, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("eieren", 2, "stuks"))
    recept3.voeg_ingredient_toe(Ingredient("Parmezaanse kaas", 50, "gram"))

    recept3.voeg_stap_toe(Stap("Kook de pasta volgens de aanwijzingen op de verpakking."))
    recept3.voeg_stap_toe(Stap("Bak het spek in een pan tot het knapperig is."))
    recept3.voeg_stap_toe(Stap("Kluts de eieren in een kom en meng de Parmezaanse kaas erdoor."))
    recept3.voeg_stap_toe(Stap("Giet de pasta af en meng deze met het spek en het eiermengsel. Serveer direct."))

    recepten.append(recept2)
    recepten.append(recept3)

    for recept in recepten:
        print(f"Recept: {recept._Recept__naam}")
        print(f"Omschrijving: {recept._Recept__omschrijving}")
        print(f"Ingredienten:")
        for ingredient in recept._Recept__ingredient_list:
            print(f"  - {ingredient}")
        print(f"Stappen:")
        for i, stap in enumerate(recept._Recept__stappen, 1):
            print(f"  {i}. {stap}")
        print()

if __name__ == "__main__":
    main()