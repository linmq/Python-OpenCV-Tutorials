import numpy as np
import cv2
 
cap = cv2.VideoCapture('1.avi')
img2 = cv2.imread('mainlogo.png', cv2.IMREAD_COLOR)
rows,cols,channels = img2.shape
print(rows)
print(cols)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 25, (768,1024))
 
while(cap.isOpened()):
    ret, img1 = cap.read()
    if ret==True:
        #img1 = cv2.flip(img1,0)

        roi = img1[0:rows, 0:cols]
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

        img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

        dst = cv2.add(img1_bg, img2_fg)
        img1[0:rows, 0:cols ] = dst

        out.write(img1)

        #cv2.imshow('frame', img1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
print('out.release')
cv2.destroyAllWindows()