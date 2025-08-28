from fpdf import FPDF
import random

# Create a PDF object
pdfq = FPDF()
pdfa = FPDF()
pdfq.add_page()
pdfa.add_page()

pdfq.set_font("Arial", size=12)
pdfa.set_font("Arial", size=12)

questCombos = set()
x = random.randint(1, 24)
y = random.randint(1, 24)
Qnum = 1

Qamount = int(input("How many questions would you like? "))

def check(a, b):
    return a / b == 1

def search(x, y):
    return (x, y) not in questCombos

pdfq.cell(200, 10, txt="Math Practice(80 Questions)", ln=True, align="C")
pdfq.cell(100, 10, txt="Name:                              is silly", ln=True, align="C")

def genmath(void):
    for i in range(0, (Qamount - (Qamount % 4))/4):
        for j in range(1, 5):
            if (Qnum == Qamount):
                return
            
            while (search(x, y) != True):
                x = random.randint(1, 24)
                y = random.randint(1, 24)

            equationP = f"{Qnum}. {x} x {y} = "
            answerP = f"{Qnum}. {x*y}"
            pdfq.cell(50, 30, txt=equationP, ln=check(4, j), align="L")
            pdfa.cell(50, 10, txt=answerP, ln=check(4, j), align="L")
            questCombos.add((x, y))
            Qnum += 1


genmath()
pdfq.output("MathPractice_1.pdf")
pdfa.output("MathAnswer_1.pdf")