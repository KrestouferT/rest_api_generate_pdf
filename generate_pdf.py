#!/usr/bin/env python
# -*- coding: utf-8 -*-
import reportlab.rl_config
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

reportlab.rl_config.warnOnMissingFontGlyphs = 0
pdfmetrics.registerFont(TTFont('Arial', 'fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'fonts/Arial-Bold.ttf'))


def generate_pdf(vorname, nachname, strasse, plz, stadt, rufnummer):
    c = canvas.Canvas("generated_pdf/" + f"{vorname}_{nachname}.pdf", pagesize=A4)
    c.setFont('Arial-Bold', 15, leading=None)
    c.drawString(30, 780, vorname + " " + nachname)
    c.setFont('Arial', 15, leading=None)
    c.drawString(30, 760, strasse)
    c.drawString(30, 740, plz + " " + stadt)
    c.drawString(30, 660, "Telefónica O2 Germany GmbH & Co. OHG")
    c.drawString(30, 640, "Kundenbetreuung")
    c.drawString(30, 620, "90345 Nürnberg")
    c.drawString(30, 590, "vorab per FAX an 01805 - 57 17 66")
    datum = time.strftime("%d-%m-%Y", time.localtime())
    c.drawString(450, 780, f"Datum: {datum} ")
    c.drawString(30, 510, "Rufnummer: " + rufnummer)
    c.drawString(30, 460, "O2 Kündigung")
    c.drawString(30, 400, "Sehr geehrte Damen und Herren,")
    c.drawString(30, 380, "hiermit kündige ich meinen O2-Vertrag fristgerecht zum nächstmöglichen Zeitpunkt. ")
    c.drawString(30, 360, "Bitte senden Sie mir eine schriftliche Bestätigung der Kündigung unter Angabe des ")
    c.drawString(30, 340, "Beendigungszeitpunktes zu.")
    c.drawString(30, 275, "Mit freundlichen Grüßen")
    c.drawString(30, 230, vorname + ' ' + nachname)
    c.showPage()
    c.save()
    return "generated_pdf/" + f"{vorname}_{nachname}.pdf"
