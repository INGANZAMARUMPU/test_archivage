from pathlib import Path
import subprocess
from pdf2jpg import pdf2jpg
import sys
import filetype
import shutil

fichier = Path(sys.argv[1])

accepted_mine = [
    "image/png",
    "image/jpeg",
    "application/pdf"
]

kind = filetype.guess(fichier)

if not kind.mime in accepted_mine:
    f = '\n '.join(accepted_mine)
    print(f"{kind.mime} Non prise en charge.\n Seul les formats {f} \nsont prise en charge")
    exit()

image_path:Path = None

if(kind.mime == "application/pdf"):
    image_path = fichier.parent
    result = pdf2jpg.convert_pdf2jpg(fichier, image_path, pages="ALL")
else:
    new_path:Path = fichier.parent / (str(fichier.stem)+".pdf_dir/")
    if not new_path.exists:
        new_path.mkdir()
    image_path = new_path
    shutil.copyfile(str(fichier), new_path/('0_'+fichier.name))

for item in image_path.iterdir():
    print(item)
    print("_"*len(str(item)))
    content = subprocess.check_output([
        f"./tesseract", "-l", "fra", item, "stdout"
    ]).decode()
    print(content)