#coding:utf-8

import cv2
import numpy as np

class opencvSample:

    def __init__(self, sourceimage):
        self.sourceimage = sourceimage

    def match(self, templateimage, threshold=0.8):
        image = cv2.imread(self.sourceimage)
        template = cv2.imread(templateimage)
        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        similarity = cv2.minMaxLoc(result)[1]
        if similarity < threshold:
            return similarity
        else:
            return np.unravel_index(result.argmax(), result.shape)

if __name__ == '__main__':
    matcher = opencvSample('./fixture/T-Shirt.jpg')
    for item in ['./fixture/T-Shirt-logo.jpg', './fixture/logo.png']:
        print(item, matcher.match(item))

