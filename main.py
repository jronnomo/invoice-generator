import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('./invoices/*xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)

    pdf.add_page()
    filename = Path(filepath).stem
    invoice, date = filename.split('-')

    year, month, day = date.split('.')

    pdf.set_font("Times", "B", 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=20, txt=f"Invoice Nr. {invoice}", align="L")

    pdf.ln(10)
    pdf.set_font("Times", "", 15)
    pdf.cell(w=0, h=15, txt=f"Date: {month}-{day}-{year}", align="L")

    pdf.ln(15)
    pdf.set_font("Times", "B", 14)
    for column in df.columns:
        title = column.replace("_", " ").title()
        pdf.cell(w=float(len(title))*3.1, h=10, txt=f"{title}", align="L", border=True)

    pdf.set_font("Times", "", 9)
    for index, row in df.iterrows():
        pdf.ln(10)
        for column in df.columns:
            title = column.replace("_", " ").title()
            pdf.cell(w=float(len(title)) * 3.1, h=10, txt=f"{df[column][index]}", align="L", border=True)

    pdf.ln(10)
    total_price = str(df['total_price'].sum())
    for column in df.columns:
        title = column.replace("_", " ").title()
        if title == "Total Price":
            pdf.cell(w=float(len(title)) * 3.1, h=10, txt=total_price, align="L", border=True)
        else:
            pdf.cell(w=float(len(title)) * 3.1, h=10, txt="", align="L", border=True)

# Add Total Sum sentence
    pdf.ln(15)
    pdf.set_font("Times", "B", 12)
    pdf.cell(w=0, h=12, txt=f"The total price of the order is {total_price}")

# Add company logo
    pdf.ln(9)
    pdf.set_font("Times", "B", 10)
    pdf.cell(w=20, h=12, txt="PythonHow")
    pdf.image('images/pythonhow.png', w=5)

    pdf.output(f"./PDFs/{filename}.pdf")