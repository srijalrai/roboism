import cv2 as cv
import numpy as np
import cv2.aruco as aruco 

def rotate(img, angle): 
    (height, width) = img.shape[:2]
    rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

def addArucoImage(box, img, arucoImg):           
    h, w = arucoImg.shape[:2]                             
    point1 = box                                     
    point2 = np.float32([[0,0], [w,0], [w,h], [0,h]])
    matrix, _ = cv.findHomography(point2, point1)  
    imgOut = cv.warpPerspective(arucoImg, matrix, (img.shape[1], img.shape[0]))
    cv.fillConvexPoly(img, point1.astype(int), (0, 0, 0))
    img = img + imgOut
    return img

def cropAruco(arucoImg):
    gray = cv.cvtColor(arucoImg, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(gray, 30, 200)
    c, h = cv.findContours(edged,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    rect1=cv.minAreaRect(c[0])
    wm=rotate(arucoImg, rect1[2])
    area1=rect1[1][1]*rect1[1][0]
    
    gray1 = cv.cvtColor(wm, cv.COLOR_BGR2GRAY)
    edged1 = cv.Canny(gray1, 30, 200)
    contours, hier = cv.findContours(edged1,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    l=[]
    for k in range(len(contours)):
        l.append(abs(cv.contourArea(contours[k])-area1))

    ind=l.index(min(l))
    k1=contours[ind]

    xoff1,yoff1,w1,h1 = cv.boundingRect(k1)
    x_end1 = int(xoff1 + w1)
    y_end1= int(yoff1 + h1)
    wm=wm[yoff1:y_end1,xoff1:x_end1]
    return wm


def placeArucoOnSquare(img, upperBound, lowerBound, arucoImg):
    cropped = cropAruco(arucoImg)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    mask = cv.inRange(gray, upperBound, lowerBound)

    cont, hier = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for cnt in cont: 
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.1 * peri, True)
        
        if len(approx) == 4 and cv.contourArea(cnt) > 10000:
            rect = cv.minAreaRect(cnt)
            diff_in_dmension = rect[1][0] - rect[1][1]
            if np.absolute(diff_in_dmension) < 10: 
                box = cv.boxPoints(rect)
                box = np.float32(box)
                img = addArucoImage(box, img, cropped)
                return img

img = cv.imread('Photos/CVtask.jpg')
arucoImg = cv.imread('Photos/LMAO.jpg')
img = placeArucoOnSquare(img, 170, 180, arucoImg)

arucoImg = cv.imread('Photos/XD.jpg')
img = placeArucoOnSquare(img, 145, 150, arucoImg)

arucoImg = cv.imread('Photos/HaHa.jpg')
img = placeArucoOnSquare(img, -1, 5, arucoImg)

arucoImg = cv.imread('Photos/Ha.jpg')
img = placeArucoOnSquare(img, 220, 225, arucoImg)

cv.imshow('Final Image', img)

cv.waitKey(0)
