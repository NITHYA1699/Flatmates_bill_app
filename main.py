from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Enter bill amount: "))
period = input("Enter period of stay (eg. July 2021): ")

name1 = input("What is your name?")
days_stayed1 = int(input(f"How many days did {name1} stay in the house during the bill period?"))
name2 = input("What is your flatmate's name?")
days_stayed2 = int(input(f"How many days did your flatmate {name2} stay in the house during the bill period?"))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_stayed1)
flatmate2 = Flatmate(name2, days_stayed2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport("report1.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)
