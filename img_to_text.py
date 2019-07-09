import pytesseract
import nltk
import matplotlib
from nltk.corpus import wordnet
from PIL import Image
img=Image.open("quote.jpg") 
result=pytesseract.image_to_string(img)
print(result)
