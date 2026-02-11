from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram", altenatief='tofu', kcal=150))
    recept1.voeg_ingredient_toe(Ingredient("rijst", 300, "gram", kcal=120))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram",  kcal=80))

    recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen.", tip="Gebruik een rijstkoker voor perfect gekookte rijst."))
    recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even).", tip="Gebruik kipfilet voor een malse kip Kerrie."))

    recepten.append(recept1)

    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")
    recept2.voeg_ingredient_toe(Ingredient("gehakt", 500, "gram", altenatief='plantaardige gehakt', kcal=200))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 2, "stuks", kcal=50))

    recept2.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden.", tip="Zorg dat de oven goed op temperatuur is ingesteld."))
    recept2.voeg_stap_toe(Stap("Bak het gehakt rul in een pan en voeg de gesneden paprika toe.", tip="Gebruik een pan met een dunne bodem voor gelijkmatige verwarming."))

    recepten.append(recept2)

    recept3 = Recept("Pasta Carbonara", "Een klassieke Italiaanse pasta met spek en kaas.")
    recept3.voeg_ingredient_toe(Ingredient("pasta", 400, "gram", kcal=150))
    recept3.voeg_ingredient_toe(Ingredient("spek", 200, "gram", altenatief='plantaardige spek', kcal=250))

    recept3.voeg_stap_toe(Stap("Kook de pasta volgens de aanwijzingen op de verpakking.", tip="Gebruik een grote pan met veel water voor perfecte pasta."))
    recept3.voeg_stap_toe(Stap("Bak het spek krokant in een pan.", tip="Gebruik een pan met een dunne bodem voor gelijkmatige verwarming."))

    recepten.append(recept3)
    
    for recept in recepten:
        print(f"Hoeveel personen wil je {recept._Recept__naam} maken?")
        aantal_personen = int(input())
        recept.schaal_recept(aantal_personen)

        print("Wil je de plantaardige alternatieven zien? (ja/nee)")
        antwoord = input().lower()

        print(f"\nRecept: {recept._Recept__naam}")
        print(f"Omschrijving: {recept._Recept__omschrijving}")

        print("\nStappen:")
        for stap in recept._Recept__stappen:
            print(f"  - {stap}")

        print("\nIngrediënten:")
        toon_alternatief = antwoord == "ja"

        for ingredient in recept._Recept__ingredient_list:
            print(f"  - {ingredient.__str__(toon_alternatief=toon_alternatief)}")

        print(f"\nTotaal kcal: {recept.bereken_totaal_kcal()}")
        print("\n" + "-"*40 + "\n")


if __name__ == "__main__":
    main()
