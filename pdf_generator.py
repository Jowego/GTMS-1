from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf(ga_score, rs_score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Ihre Golf Talent Magnet Score Auswertung", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Golf Attraction Score: {ga_score} / 15", ln=True)
    pdf.cell(200, 10, txt=f"Recruiting Score: {rs_score} / 20", ln=True)

    pdf.ln(10)
    if ga_score >= 12 and rs_score >= 16:
        quadrant = "Star: Digitalisierung & Attraktivität vereint"
    elif ga_score < 12 and rs_score >= 16:
        quadrant = "Recruiting-Profi: Jetzt Golfpotenzial aktivieren"
    elif ga_score >= 12 and rs_score < 16:
        quadrant = "Golftalent: Jetzt Recruiting digitalisieren"
    else:
        quadrant = "Hidden Champion im Aufbau"

    pdf.multi_cell(0, 10, txt=f"Ihre Einordnung in der BCG-Matrix: {quadrant}")

    filename = f"/mnt/data/GTMS_Ergebnis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    return filename
