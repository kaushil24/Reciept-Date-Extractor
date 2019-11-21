import pytesseract as ptr
from PIL import Image
import os



class TesseractTxtExtractor():

    def extractTxt(self,imgNme):
        loc = os.path.join("Sample Dataset", "Receipts")
        st = ptr.image_to_string(os.path.join(loc, imgNme))
        return st

if __name__=="__main__":

    tx = TesseractTxtExtractor()
    st = tx.extractTxt("1ae93f0a.jpeg")
    print(st)