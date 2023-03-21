from pathlib import Path
from pdf2jpg import pdf2jpg
import sys
import filetype
import shutil

fichier = Path(sys.argv[1])

kind = filetype.guess(fichier)
print('File MIME type: %s' % kind.mime)

pdf = None

if(kind.mime == "application/pdf"):
    result = pdf2jpg.convert_pdf2jpg(fichier, fichier.parent, pages="ALL")
else:
    new_path:Path = fichier.parent / (str(fichier.stem)+".pdf_dir/")
    new_path.mkdir()
    shutil.copyfile(str(fichier), new_path/('0_'+fichier.name))
