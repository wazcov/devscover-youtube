from PIL import Image
img =Image.open (‘1.png’)
text = pytesseract.image_to_string(img, config=’’)
print (text)