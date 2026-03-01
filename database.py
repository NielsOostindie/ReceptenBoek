import sqlite3
from ingredient import Ingredient
from stap import Stap
from recept import Recept

DB_FILE = "recepten.db"


def maak_verbinding():
    return sqlite3.connect(DB_FILE)


def initialiseer_database():
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS recept (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            omschrijving TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS ingredient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER NOT NULL,
            naam TEXT NOT NULL,
            hoeveelheid REAL NOT NULL,
            eenheid TEXT NOT NULL,
            kcal INTEGER NOT NULL,
            alternatief_naam TEXT,
            alternatief_hoeveelheid REAL,
            alternatief_eenheid TEXT,
            alternatief_kcal INTEGER,
            FOREIGN KEY (recept_id) REFERENCES recept(id)
        );

        CREATE TABLE IF NOT EXISTS stap (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER NOT NULL,
            volgorde INTEGER NOT NULL,
            beschrijving TEXT NOT NULL,
            tip TEXT,
            FOREIGN KEY (recept_id) REFERENCES recept(id)
        );
    """)

    conn.commit()
    conn.close()


def sla_recept_op(recept: Recept):
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO recept (naam, omschrijving) VALUES (?, ?)",
        (recept.get_naam(), recept.get_omschrijving())
    )
    recept_id = cursor.lastrowid

    for ing in recept.get_ingredienten():
        alternatief = ing.get_plantaardig_alternatief()
        cursor.execute(
            """INSERT INTO ingredient 
               (recept_id, naam, hoeveelheid, eenheid, kcal,
                alternatief_naam, alternatief_hoeveelheid, alternatief_eenheid, alternatief_kcal)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                recept_id,
                ing.get_naam(), ing.get_hoeveelheid(), ing.get_eenheid(), ing.get_kcal(),
                alternatief.get_naam() if alternatief else None,
                alternatief.get_hoeveelheid() if alternatief else None,
                alternatief.get_eenheid() if alternatief else None,
                alternatief.get_kcal() if alternatief else None,
            )
        )

    for i, stap in enumerate(recept.get_stappen(), 1):
        cursor.execute(
            "INSERT INTO stap (recept_id, volgorde, beschrijving, tip) VALUES (?, ?, ?, ?)",
            (recept_id, i, stap.get_beschrijving(), stap.get_tip())
        )

    conn.commit()
    conn.close()


def verwijder_recept_uit_db(naam: str):
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM recept WHERE naam = ?", (naam,))
    rij = cursor.fetchone()
    if rij:
        recept_id = rij[0]
        cursor.execute("DELETE FROM ingredient WHERE recept_id = ?", (recept_id,))
        cursor.execute("DELETE FROM stap WHERE recept_id = ?", (recept_id,))
        cursor.execute("DELETE FROM recept WHERE id = ?", (recept_id,))

    conn.commit()
    conn.close()


def laad_recepten() -> list:
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute("SELECT id, naam, omschrijving FROM recept")
    recept_rijen = cursor.fetchall()

    recepten = []
    for recept_id, naam, omschrijving in recept_rijen:
        recept = Recept(naam, omschrijving)

        cursor.execute(
            "SELECT naam, hoeveelheid, eenheid, kcal, alternatief_naam, alternatief_hoeveelheid, alternatief_eenheid, alternatief_kcal FROM ingredient WHERE recept_id = ?",
            (recept_id,)
        )
        for rij in cursor.fetchall():
            ing = Ingredient(rij[0], rij[1], rij[2], rij[3])
            if rij[4]:
                ing.set_plantaardig_alternatief(Ingredient(rij[4], rij[5], rij[6], rij[7]))
            recept.voeg_ingredient_toe(ing)

        cursor.execute(
            "SELECT beschrijving, tip FROM stap WHERE recept_id = ? ORDER BY volgorde",
            (recept_id,)
        )
        for beschrijving, tip in cursor.fetchall():
            recept.voeg_stap_toe(Stap(beschrijving, tip))

        recepten.append(recept)

    conn.close()
    return recepten