from recept import Recept
from ingredient import Ingredient
from stap import Stap


def maak_startrecepten():
    recepten = []

    # Recept 1: Kip Kerrie
    r1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes.")
    kip = Ingredient("Kipfilet", 150, "gram", 165)
    kip.set_plantaardig_alternatief(Ingredient("Tofu", 150, "gram", 120))
    r1.voeg_ingredient_toe(kip)
    r1.voeg_ingredient_toe(Ingredient("Sperziebonen", 100, "gram", 35))
    r1.voeg_ingredient_toe(Ingredient("Basmatirijst", 75, "gram", 265))
    r1.voeg_ingredient_toe(Ingredient("Kerriepoeder", 2, "tl", 14))
    r1.voeg_ingredient_toe(Ingredient("Kokosmelk", 100, "ml", 230))
    r1.voeg_stap_toe(Stap("Kook de rijst.", "Spoel eerst af voor luchtigere rijst."))
    r1.voeg_stap_toe(Stap("Kook de sperziebonen 5 minuten en giet af."))
    r1.voeg_stap_toe(Stap("Fruit gesnipperde ui en knoflook in olie."))
    r1.voeg_stap_toe(Stap("Bak de kip goudbruin en voeg kerriepoeder toe."))
    r1.voeg_stap_toe(Stap("Voeg kokosmelk toe en laat 10 minuten sudderen.", "Scheutje limoensap geeft extra frisheid."))
    r1.voeg_stap_toe(Stap("Serveer de kerrie op rijst met sperziebonen ernaast."))
    recepten.append(r1)

    # Recept 2: Gehakt quiche met paprika
    r2 = Recept("Gehakt quiche met paprika", "Een stevige quiche met gehakt en paprika.")
    gehakt = Ingredient("Rundergehakt", 125, "gram", 280)
    gehakt.set_plantaardig_alternatief(Ingredient("Plantaardige gehakt", 125, "gram", 190))
    r2.voeg_ingredient_toe(gehakt)
    r2.voeg_ingredient_toe(Ingredient("Rode paprika", 0.5, "stuk", 25))
    r2.voeg_ingredient_toe(Ingredient("Quichebodem", 0.25, "rol", 180))
    ei = Ingredient("Ei", 1, "stuk", 70)
    ei.set_plantaardig_alternatief(Ingredient("Aquafaba", 3, "el", 10))
    r2.voeg_ingredient_toe(ei)
    r2.voeg_ingredient_toe(Ingredient("Geraspte kaas", 30, "gram", 120))
    r2.voeg_ingredient_toe(Ingredient("Slagroom", 50, "ml", 175))
    r2.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden."))
    r2.voeg_stap_toe(Stap("Bekleed een quichevorm met deeg en prik gaatjes.", "Blind bakken met bakpapier houdt de bodem knapperig."))
    r2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg gesneden paprika toe."))
    r2.voeg_stap_toe(Stap("Klop ei los met slagroom, zout en peper."))
    r2.voeg_stap_toe(Stap("Verdeel gehakt over de bodem, giet eimengsel erover en strooi kaas erop."))
    r2.voeg_stap_toe(Stap("Bak 30-35 minuten tot de vulling gestold en goudbruin is."))
    recepten.append(r2)

    # Recept 3: Pasta Carbonara
    r3 = Recept("Pasta Carbonara", "Een klassieke Italiaanse pasta, romig en hartig.")
    spek = Ingredient("Pancetta", 50, "gram", 210)
    spek.set_plantaardig_alternatief(Ingredient("Gerookte champignons", 80, "gram", 30))
    r3.voeg_ingredient_toe(Ingredient("Spaghetti", 100, "gram", 350))
    r3.voeg_ingredient_toe(spek)
    r3.voeg_ingredient_toe(Ingredient("Eidooier", 1, "stuk", 55))
    r3.voeg_ingredient_toe(Ingredient("Parmezaan", 30, "gram", 120))
    r3.voeg_ingredient_toe(Ingredient("Zwarte peper", 1, "tl", 5))
    r3.voeg_stap_toe(Stap("Kook de spaghetti al dente en bewaar een kopje kookwater."))
    r3.voeg_stap_toe(Stap("Bak de pancetta krokant in een droge pan."))
    r3.voeg_stap_toe(Stap("Klop eidooiers met parmezaan en peper.", "Gebruik eieren op kamertemperatuur."))
    r3.voeg_stap_toe(Stap("Haal pan van het vuur, voeg pasta en eimengsel toe en meng snel.", "Pan van het vuur! Anders stolt het ei."))
    r3.voeg_stap_toe(Stap("Serveer direct met extra parmezaan en peper."))
    recepten.append(r3)

    return recepten


def vraag_ja_nee(vraag):
    while True:
        antwoord = input(f"{vraag} (ja/nee): ").strip().lower()
        if antwoord in ("ja", "nee"):
            return antwoord == "ja"
        print("Foutieve invoer.")


def toon_menu():
    print("\n=== RECEPTENBOEK ===")
    print("1. Toon recept")
    print("2. Voeg recept toe")
    print("3. Afsluiten")


def selecteer_recept(recepten):
    if not recepten:
        print("Geen recepten beschikbaar.")
        return None
    print()
    for i, r in enumerate(recepten, 1):
        print(f"  {i}. {r.get_naam()}")
    while True:
        try:
            keuze = int(input("\nSelecteer een recept (nummer): "))
            if 1 <= keuze <= len(recepten):
                return recepten[keuze - 1]
            print("Recept niet gevonden.")
        except ValueError:
            print("Foutieve invoer.")


def toon_flow(recepten):
    recept = selecteer_recept(recepten)
    if recept is None:
        return

    while True:
        try:
            aantal = int(input("Voor hoeveel personen? "))
            if aantal > 0:
                break
            print("Foutieve invoer.")
        except ValueError:
            print("Foutieve invoer.")

    recept.set_aantal_personen(aantal)

    plantaardig = False
    if any(ing.heeft_plantaardig_alternatief() for ing in recept.get_ingredienten()):
        plantaardig = vraag_ja_nee("Wil je de plantaardige versie?")

    recept.toon_recept(plantaardig)

    print("\n1. Verwijder dit recept")
    print("2. Terug naar menu")
    while True:
        keuze = input("Keuze: ").strip()
        if keuze == "1":
            if vraag_ja_nee(f"Weet je zeker dat je '{recept.get_naam()}' wilt verwijderen?"):
                recepten.remove(recept)
                print("Recept verwijderd.")
            return
        elif keuze == "2":
            return
        else:
            print("Foutieve invoer.")


def voeg_ingredient_in(label="Ingrediënt"):
    print(f"\n-- {label} --")
    naam = input("  Naam: ").strip()
    while True:
        try:
            hoeveelheid = float(input("  Hoeveelheid: "))
            break
        except ValueError:
            print("  Foutieve invoer.")
    eenheid = input("  Eenheid (gram/ml/stuk/tl): ").strip()
    while True:
        try:
            kcal = int(input("  Kcal: "))
            break
        except ValueError:
            print("  Foutieve invoer.")
    return Ingredient(naam, hoeveelheid, eenheid, kcal)


def toevoegen_flow(recepten):
    print("\n--- Nieuw recept toevoegen ---")
    naam = input("Naam: ").strip()
    omschrijving = input("Omschrijving: ").strip()
    nieuw = Recept(naam, omschrijving)

    print("\n-- Ingrediënten --")
    while True:
        ingredient = voeg_ingredient_in()
        if vraag_ja_nee("  Plantaardig alternatief toevoegen?"):
            alternatief = voeg_ingredient_in("Plantaardig alternatief")
            ingredient.set_plantaardig_alternatief(alternatief)
        nieuw.voeg_ingredient_toe(ingredient)
        if not vraag_ja_nee("Nog een ingrediënt toevoegen?"):
            break

    print("\n-- Bereidingsstappen --")
    while True:
        beschrijving = input("Stap: ").strip()
        tip = None
        if vraag_ja_nee("Tip toevoegen?"):
            tip = input("Tip: ").strip()
        nieuw.voeg_stap_toe(Stap(beschrijving, tip))
        if not vraag_ja_nee("Nog een stap toevoegen?"):
            break

    recepten.append(nieuw)
    print(f"\nRecept '{naam}' toegevoegd!")
    nieuw.toon_recept()


def main():
    recepten = maak_startrecepten()

    while True:
        toon_menu()
        keuze = input("Keuze: ").strip()

        if keuze == "1":
            toon_flow(recepten)
        elif keuze == "2":
            toevoegen_flow(recepten)
        elif keuze == "3":
            print("Tot ziens!")
            break
        else:
            print("Foutieve invoer. Kies 1, 2 of 3.")


if __name__ == "__main__":
    main()