import webbrowser

from fpdf import FPDF


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2)))

        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1)))
        pdf = FPDF(orientation='P', unit='pt', format='A4')  # 12pt=16pixels
        pdf.add_page()

        pdf.image("unnamed.png", w=100, h=100)

        pdf.set_font(family='Times', size=12)  # bold
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)  # centrealign

        pdf.cell(w=150, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.cell(w=150, h=40, txt="Name of the flatmate", border=1)
        pdf.cell(w=150, h=40, txt="Amount to be paid", border=1, ln=1)

        pdf.cell(w=150, h=30, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=30, txt=flatmate1_pay, border=1, ln=1)

        pdf.cell(w=150, h=30, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=30, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)