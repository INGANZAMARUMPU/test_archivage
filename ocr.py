from pathlib import Path
from pdf2jpg import pdf2jpg
import sys
import filetype
import shutil

fichier = Path(sys.argv[1])

accepted_mine = [
    "image/png",
    "application/pdf",
    "application/jpeg"
]

kind = filetype.guess(fichier)
print('File MIME type: %s' % kind.mime)

if(not kind.mime in accepted_mine):
    raise Exception("Format non prise en charge")

if(kind.mime == "application/pdf"):
    result = pdf2jpg.convert_pdf2jpg(fichier, fichier.parent, pages="ALL")
else:
    new_path:Path = fichier.parent / (str(fichier.stem)+".pdf_dir/")
    new_path.mkdir()
    shutil.copyfile(str(fichier), new_path/('0_'+fichier.name))
