import pytesseract as ptr
from PIL import Image
import os
import numpy as np


class TesseractTxtExtractor():

    def extractTxt(self,imgNme = '', imgMtx = ''):
        loc = os.path.join("Sample Dataset", "Receipts")
        
        if imgNme:
            loc = os.path.join("Sample Dataset", "Receipts")
            st = ptr.image_to_string(os.path.join(loc, imgNme))
            return st
        
        elif imgMtx:
            st = ptr.image_to_string(imgMtx)
            return st

        else:
            print("***********No Image Name or Location found****************")

if __name__=="__main__":

    tx = TesseractTxtExtractor()
    st = tx.extractTxt("1ae93f0a.jpeg")
    print(st)