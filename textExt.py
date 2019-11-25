import pytesseract as ptr
from PIL import Image
import os
import numpy as np


class TesseractTxtExtractor():

    def extractTxt(self, imgMtx = '', imgNme = ''):
        loc = os.path.join("Sample Dataset", "Receipts")
        
        if imgNme:
            loc = os.path.join("Sample Dataset", "Receipts")
            st = ptr.image_to_string(os.path.join(loc, imgNme), config="--psm 6")
            return st
        
        elif len(imgMtx):
            st = ptr.image_to_string(imgMtx) #, config="--oem 1")
            return st

        else:
            print("***********No Image Name or Location found****************")

if __name__=="__main__":

    tx = TesseractTxtExtractor()
    st = tx.extractTxt(imgNme="04fa5e11.jpeg")
    print(st)