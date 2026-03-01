from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER


def genereer_pdf(recept, plantaardig: bool = False, bestandsnaam: str = None):
    if bestandsnaam is None:
        veilige_naam = recept.get_naam().replace(" ", "_").lower()
        bestandsnaam = f"{veilige_naam}.pdf"

    doc = SimpleDocTemplate(
        bestandsnaam,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    styles = getSampleStyleSheet()

    titel_stijl = ParagraphStyle(
        "Titel",
        parent=styles["Title"],
        fontSize=24,
        textColor=colors.HexColor("#2d6a4f"),
        spaceAfter=6,
        alignment=TA_CENTER,
    )
    ondertitel_stijl = ParagraphStyle(
        "Ondertitel",
        parent=styles["Normal"],
        fontSize=11,
        textColor=colors.HexColor("#555555"),
        spaceAfter=16,
        alignment=TA_CENTER,
    )
    sectie_stijl = ParagraphStyle(
        "Sectie",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=colors.HexColor("#2d6a4f"),
        spaceBefore=14,
        spaceAfter=6,
    )
    ingredient_stijl = ParagraphStyle(
        "Ingredient",
        parent=styles["Normal"],
        fontSize=10,
        leftIndent=12,
        spaceAfter=3,
    )
    stap_stijl = ParagraphStyle(
        "Stap",
        parent=styles["Normal"],
        fontSize=10,
        leftIndent=12,
        spaceAfter=4,
    )
    tip_stijl = ParagraphStyle(
        "Tip",
        parent=styles["Normal"],
        fontSize=9,
        leftIndent=24,
        textColor=colors.HexColor("#b5651d"),
        spaceAfter=6,
        fontName="Helvetica-Oblique",
    )
    kcal_stijl = ParagraphStyle(
        "Kcal",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#555555"),
        spaceBefore=12,
        alignment=TA_CENTER,
    )

    inhoud = []

    # Titel
    inhoud.append(Paragraph(recept.get_naam(), titel_stijl))
    inhoud.append(Paragraph(recept.get_omschrijving(), ondertitel_stijl))
    inhoud.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2d6a4f")))
    inhoud.append(Spacer(1, 12))

    # Personen info
    inhoud.append(Paragraph(f"Personen: {recept.get_aantal_personen()}", ondertitel_stijl))

    # Ingrediënten
    inhoud.append(Paragraph("Ingrediënten", sectie_stijl))
    for ing in recept.get_plantaardig_recept(plantaardig):
        inhoud.append(Paragraph(f"• {ing}", ingredient_stijl))

    # Bereidingsstappen
    inhoud.append(Paragraph("Bereidingsstappen", sectie_stijl))
    for i, stap in enumerate(recept.get_stappen(), 1):
        inhoud.append(Paragraph(f"{i}. {stap.get_beschrijving()}", stap_stijl))
        if stap.get_tip():
            inhoud.append(Paragraph(f"💡 Tip: {stap.get_tip()}", tip_stijl))

    # Kcal
    inhoud.append(Spacer(1, 12))
    inhoud.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2d6a4f")))
    inhoud.append(Paragraph(f"Totaal: {recept.get_totaal_kcal(plantaardig)} kcal", kcal_stijl))

    doc.build(inhoud)
    return bestandsnaam