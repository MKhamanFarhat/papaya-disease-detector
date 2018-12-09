import cv2 as cv
import argparse
import numpy as np
import wholePapaya
from matplotlib import pyplot as plt

def main():
    # Load source image
    parser = argparse.ArgumentParser(description='PAPAYA DISEASE DETECTION.')
    parser.add_argument('-i', '--input', help='Path to input image.', default='assets/145-046.bmp')
    args = parser.parse_args()

    src = cv.imread(args.input)
    cv.namedWindow('1',cv.WINDOW_NORMAL)
    cv.resizeWindow('1',600,600)
    cv.imshow('1', src)
    print("Image %s loaded" % args.input)
    # cv.waitKey(1000)

    # Segment whole papaya
    full_papaya = wholePapaya.papayaSegment(src)
    cv.namedWindow('2',cv.WINDOW_NORMAL)
    cv.resizeWindow('2',600,600)
    cv.imshow('2',full_papaya)
    cv.waitKey(1300)
    print("Whole papaya segmented")

    ret, thresh = cv.threshold(full_papaya, 1,1,1)
    contours, hierarchy = cv.findContours(thresh, 1, 2)

    cnt = contours[0]
    M = cv.moments(cnt)
    print (M)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.namedWindow(window_detection_name,cv.WINDOW_NORMAL)
    cv.drawContours(src, contours, -1, (255,0,5), 1)




    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
