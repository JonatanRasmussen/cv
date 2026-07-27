from pypdf import PdfReader, PdfWriter
import os

base_path = r"C:\Users\BudoB\OneDrive\Dokumenter Tekst\Personlig\Joblog"
pdf_1_path = os.path.join(base_path, "MSc_diploma_and_grades_JonatanRasmussen.pdf")
pdf_2_path = os.path.join(base_path, "BSc_diploma_and_grades_JonatanRasmussen.pdf")
output_path = os.path.join(base_path, "MSc+BSc_MERGED_diploma_and_grades_JonatanRasmussen.pdf")

writer: PdfWriter = PdfWriter()
pdf_1_reader: PdfReader = PdfReader(stream=pdf_1_path)
for page in pdf_1_reader.pages:
    writer.add_page(page)
pdf_2_reader: PdfReader = PdfReader(stream=pdf_2_path)
for page in pdf_2_reader.pages:  # To only include the first 3 pages: pdf_2_reader.pages[:3]:
    writer.add_page(page)
with open(file=output_path, mode="wb") as f:
    writer.write(stream=f)
print(f"PDF successfully created at:\n{output_path}")