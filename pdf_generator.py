from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(ga_score, rs_score):
    filepath = "Ergebnis_GTMS.pdf"
    c = canvas.Canvas(filepath, pagesize=A4)
    text = c.beginText(40, 800)
    text.setFont("Helvetica", 14)
    text.textLine(f"Golf Attraction Score: {ga_score}")
    text.textLine(f"Recruiting Score: {rs_score}")
    text.textLine("")
    if ga_score >= 25 and rs_score >= 25:
        text.textLine("🎯 Sie gehören zu den Stars der Digitalisierung!")
    elif ga_score >= 25:
        text.textLine("🚀 Sie sind ein digitaler Magnet mit Recruiting-Potenzial.")
    elif rs_score >= 25:
        text.textLine("🔧 Recruiting top – aber digitale Anziehung schwach.")
    else:
        text.textLine("🌱 Sie haben großes Potenzial – nutzen Sie jetzt Ihre Chance.")
    c.drawText(text)
    c.showPage()
    c.save()
    return filepath
