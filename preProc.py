from PIL import Image
import cv2 as cv
import numpy as numpy
import skimage 
import os

class preProcessor():


    def contrast(self, img, block_size = 11, C = 25):
        '''
        first arg: image matrix, block_size: 11(default), C: 25(default)
        '''
        thrsh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 25)
        return thrsh




if __name__ == "__main__":
    pp = preProcessor()

    name = "04fa5e11.jpeg"
    loc = os.path.join("Sample Dataset", "Receipts")
    img = cv.imread(os.path.join(loc, name), 0)  # The last arg 0 stands for converting img to grey scale 
    cv.imshow("Original Img", img)
    thrsh = pp.contrast(img)
    cv.imshow("Adaprive THresholding", thrsh)
    cv.waitKey(0)
    cv.destroyAllWindows()