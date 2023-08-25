import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('./invoices/*xlsx')
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    filename = Path(filepath).stem
    invoice = filename.split('-')[0]
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=f"Invoice Nr. {invoice}", align="L")
    pdf.output(f"./PDFs/{filename}.pdf")