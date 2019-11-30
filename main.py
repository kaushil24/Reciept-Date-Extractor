from dateExt import dateExtractor
from textExt import TesseractTxtExtractor
from preProc import preProcessor
import pandas as pd 
import os 
from PIL import Image
import cv2 as cv
from receiptScanner import crnn_processor


def full_Evaluation_crnn():
    loc = os.path.join("Sample Dataset", "Receipts")
    imgs = os.listdir(loc)

    output = []
    dx = dateExtractor()

    for i, img in enumerate(imgs):
        try:
            txt = crnn_processor.process_img(img)
            date = dx.extractDate(txt)
            output.append([img, date])
            print(i, ":   | ",img, ":", date)

        except Exception as e:
            print("exception occured at", img)
            print(e)
            continue

    print("*******ALLLLLLLLLL DONEEEEEE********************")

    df = pd.DataFrame(output)
    df.to_csv("Results/4 - CRNN Model/Normal Output.csv")




def full_Evaluation():
    pp = preProcessor()
    tx = TesseractTxtExtractor()
    dx = dateExtractor()
    


    loc = os.path.join("Sample Dataset", "Receipts")
    imgs  = os.listdir(loc)

    output = []
    for i,img in enumerate(imgs):
        try: 
            mtx = cv.imread(os.path.join(loc, img))
            # mtx = pp.contrast(mtx)
            content = tx.extractTxt(mtx)
            date = dx.extractDate(content)
            output.append([img, date])
            print(i, ":   | ",img, ":", date)

        except:
            print("exception occured at", img)
            continue

    print("*******ALLLLLLLLLL DONEEEEEE********************")

    df = pd.DataFrame(output)
    df.to_csv("Results/3 - auto corr in dateExt/Normal Output.csv")


if __name__ == "__main__":


    full_Evaluation_crnn()
#     pp = preProcessor()
#     tx = TesseractTxtExtractor()
#     dx = dateExtractor()
#     loc = os.path.join("Sample Dataset", "Receipts")
#     imgs  = ["2ef79975.jpeg", "04fa5e11.jpeg"]

#     output = []
#     for i,img in enumerate(imgs):
        
#         mtx = cv.imread(os.path.join(loc, img), 0)
#         cv.imshow("Normal", mtx)
#         # mtx = pp.contrast(mtx)
#         cv.imshow("Contrast", mtx)
#         content = tx.extractTxt(mtx)
#         date = dx.extractDate(content)
#         output.append([img, date])
#         print(i, ":   | ",img, ":", date)
#         cv.waitKey(0)


# cv.destroyAllWindows()

    
