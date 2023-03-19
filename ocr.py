import easyocr, sys

reader = easyocr.Reader(['fr','fr'])

result = reader.readtext(sys.argv[1], batch_size=5, rotation_info=[90])

print(" ".join([x[1] for x in result]))
# print(result)
