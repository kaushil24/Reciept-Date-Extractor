import pytesseract as ptr
from PIL import Image
import os
print("Import Successful")
class TesseractTxtExtractor():

    def extractTxt(self,imgNme):
        loc = os.path.join("Sample Dataset", "Receipts")
        st = ptr.image_to_string(os.path.join(loc, imgNme))
        return st

tx = TesseractTxtExtractor()
st = tx.extractTxt("0cc46a10.jpeg")
print(st)