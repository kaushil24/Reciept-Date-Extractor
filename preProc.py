from PIL import Image
import cv2 as cv
import numpy as numpy
import skimage 
import os
import numpy as np

class preProcessor():

    def binary(self, img):
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    def contrast(self, img, block_size = 11, C = 25):
        '''
        first arg: image matrix, block_size: 11(default), C: 25(default)
        '''
        thrsh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 25)
        return thrsh

    def dilate(self, img, x = 1, y = 1):
        kernel = np.ones((x,y), np.uint8)
        return cv.dilate(img, kernel, iterations=1)
        
    def erod(self, img, x=1, y=1):
        kernel = np.ones((x,y), np.uint8)
        erod = cv.erode(dial, kernel, iterations=1)
        return erod


    def rescale(self, img):
        return cv.resize(img, None, fx=1.75, fy=1.75, interpolation=cv.INTER_CUBIC)


    

    




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