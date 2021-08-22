class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_stayed):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill, flatmate2):
        weight = self.days_stayed / (self.days_stayed + flatmate2.days_stayed)
        to_pay = bill.amount * weight
        return to_pay