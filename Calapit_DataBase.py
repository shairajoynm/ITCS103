import openpyxl as op

wbk = op.Workbook()
sheet = wbk.active

sheet['A1']= "Book ID"
sheet['B1']= "Book Name"
sheet['C1']= "Book Author"
sheet['D1']= "Borrower Name"
sheet['E1']= "Contact Number"
sheet['F1']= "Borrow Date"
sheet['G1']= "Due Date"
sheet['H1']= "Status"
sheet['I1']= "Returned Date"
sheet['J1']= "Late Returned Fee"

sheet['A2']= 1
sheet['B2']= "Without Seeing The Dawn"
sheet['C2']= "Steven Javellana"
sheet['D2']= "Shaira Calapit"                    
sheet['E2']= int("09162898666")
sheet['F2']= "2026/11/10"
sheet['G2']= "2026/11/13"
sheet['H2']= "Borrowed"
sheet['I2']= None
sheet['J2']= 0

wbk.save("Calapit_Database.xlsx")