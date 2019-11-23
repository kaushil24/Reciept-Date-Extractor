from dateExt import dateExtractor
from textExt import TesseractTxtExtractor
import pandas as pd 
import os 
from PIL import Image
import cv2 as cv

if __name__ == "__main__":

    loc = os.path.join("Sample Dataset", "Receipts")
    print(loc[:5], len(loc))

