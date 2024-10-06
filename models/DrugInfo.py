import re

amountPattern = r"\[(?P<amount>\d+)TAB\]"
dosePattern = r"รับประทานครั้งละ\s(?P<dose>\d+)\s(?P<dosageForm>\w+)"

class DrugInfo:
    def __init__(self, genericName, dosageForm, dose, amount=10, mealTime="ก่อนอาหาร"):
        self.genericName = genericName
        self.dosageForm = dosageForm
        self.amount = amount
        self.dose = dose
        self.mealTime = mealTime
    
    @staticmethod
    def fromString(string):
        resultF = [line.strip() for line in string.splitlines() if line.strip()]

        if len(resultF) < 2:
            return None
        else: 
            genericName = resultF[0]

            amountF = re.search(amountPattern, resultF[0])
            amount = amountF.group("amount")

            doseAndDosageFormF = re.search(dosePattern, resultF[1])
            dosageForm = doseAndDosageFormF.group("dosageForm")
            dose = doseAndDosageFormF.group("dose")

            return DrugInfo(
                genericName = genericName,
                amount = int(amount),
                dosageForm = dosageForm,
                dose = int(dose)
            )