import io
import easyocr
import sys
import PyPDF2
from PyPDF2 import PdfReader
from PIL import Image

ocr_reader = easyocr.Reader(['fr','fr'])
# try:
pages_reader = PdfReader(sys.argv[1])
print(len(list(pages_reader.pages)))
for page in pages_reader.pages[4:5]:
    for image in page.images:
        i:Image = Image.fromarray(image.data)
        i.rotate(90)
        imgByteArr = io.BytesIO()
        i.save(imgByteArr)
        byte = imgByteArr.getvalue()
        result = ocr_reader.readtext(byte)
        print("\n".join([x[1] for x in result]))

# except PyPDF2.errors.PdfReadError:
#     result = ocr_reader.readtext(sys.argv[1], rotation_info=[90])
#     print("\n".join([x[1] for x in result]))
