import sys
import docx2pdf
import filetype
from pathlib import Path
from pdf2jpg import pdf2jpg

fichier = Path(sys.argv[1])

kind = filetype.guess(fichier)
print('File MIME type: %s' % kind.mime)

pdf = None

if(kind.mime == "application/pdf"):
    pdf = fichier

elif(kind.mime == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
    docx2pdf.convert(fichier.absolute(), f"{fichier.parent}.pdf")
    pdf = Path(f"{fichier.parent}.pdf")

if pdf:
    result = pdf2jpg.convert_pdf2jpg(pdf, fichier.parent, pages="ALL")
else:
    print("incovertible")

# pages_reader = PyPDF2.PdfReader(sys.argv[1])
# print(len(list(pages_reader.pages)))
# for page in pages_reader.pages[4:5]:
#     for image in page.images:
#         print()

