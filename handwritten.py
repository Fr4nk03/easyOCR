import easyocr
image = '/Users/xujincc/Documents/中山data/handwritten.jpg'
ocr = easyocr.Reader(['ch_sim', 'en'], gpu=False)
content = ocr.readtext(image, detail=0)
print(content)