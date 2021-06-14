
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

IMAGE_PATH = 'uk3.jpg'
PPMR = 0.1015625

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

image = cv2.imread(IMAGE_PATH)

scale_percent = 40 
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
orig = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

pill_cnt = max(cnts,key=cv2.contourArea)

box = cv2.minAreaRect(pill_cnt)
box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
box = np.array(box, dtype="int")
box = perspective.order_points(box)

cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

(tl, tr, br, bl) = box
(tltrX, tltrY) = midpoint(tl, tr)
(blbrX, blbrY) = midpoint(bl, br)
(tlblX, tlblY) = midpoint(tl, bl)
(trbrX, trbrY) = midpoint(tr, br)

dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

pred_dimA = dA * PPMR
pred_dimB = dB * PPMR

print("Dimensions : {:.0f}mm x {:.0f}mm".format(pred_dimA,pred_dimB))
cv2.putText(orig,"Dimensions : {:.0f}mm x {:.0f}mm".format(pred_dimA,pred_dimB),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Pill",orig)
cv2.waitKey(0)
cv2.destroyAllWindows()