import cv2 as cv
import numpy as np

trackbar_win_name = 'Bar'
width_name = 'Width'
col_name = 'Height'
switch ='0 : MASK \n1 : IMAGE'

# Elliptical Kernel
width = 3
height = 3

def row_thresh(val):
   global width
   width = val
   cv.setTrackbarPos(width_name, trackbar_win_name, width)
def col_thresh(val):
   global height
   height = val
   cv.setTrackbarPos(width_name, trackbar_win_name, height)
def nothing(x): pass

def papayaSegment(src):

   # HSV Threshold value
   low_H = 17
   high_H = 44
   low_S = 87
   high_S = 255
   low_V = 42
   high_V = 245

   imgHSV = cv.cvtColor(src, cv.COLOR_BGR2HSV)
   HSVthresh_mask = cv.inRange(imgHSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

   cv.namedWindow(trackbar_win_name, cv.WINDOW_NORMAL)
   cv.resizeWindow(trackbar_win_name, 600, 600)

   cv.createTrackbar(width_name, trackbar_win_name, 7, 200,  nothing)
   cv.createTrackbar(col_name, trackbar_win_name, 7, 200,  nothing)
   cv.createTrackbar(switch, trackbar_win_name, 0, 1,   nothing)

   # 
   global width
   global height

   # Remove items other than papaya that left from hsv filter
   while(1):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
   # get current positions of trackbars

      width = cv.getTrackbarPos(width_name, trackbar_win_name)
      height = cv.getTrackbarPos(col_name, trackbar_win_name)
      s = cv.getTrackbarPos(switch, trackbar_win_name)

      kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(width,height))
      # for removing white dots outisde papaya
      final = cv.morphologyEx(HSVthresh_mask, cv.MORPH_OPEN, kernel)



      if s == 0:
         imgOpen = final # mask
      else:
         imgOpen = cv.bitwise_and(src, src, mask=final) 

      cv.imshow(trackbar_win_name, imgOpen)
      key = cv.waitKey(50)
      if key == ord('q') or key ==13: # enter button
         break
   
   # to remove any black spots inside papaya
   while(1):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
   # get current positions of trackbars

      width = cv.getTrackbarPos(width_name, trackbar_win_name)
      height = cv.getTrackbarPos(col_name, trackbar_win_name)
      s = cv.getTrackbarPos(switch, trackbar_win_name)

      kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(width,height))
      
      final2 = cv.morphologyEx(imgOpen, cv.MORPH_CLOSE, kernel)

      if s == 0:
         imgClose = final2 # mask
      else:
         imgClose = cv.bitwise_and(src, src, mask=final2) 

      cv.imshow(trackbar_win_name, imgClose)
      key = cv.waitKey(50)
      if key == ord('q') or key ==13: # enter button
         break


   return imgClose
