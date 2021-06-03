import cv2
import numpy as np

i=np.ones((500,500,3),np.uint8)
#print(i)
#i[100:200,250:300]=255,0,0
i[:]=255,255,255
cv2.line(i,(200,200),(300,100),(0,0,0),4)
cv2.line(i,(300,100),(400,200),(0,0,0),4)
#start,end,color,thickness
cv2.rectangle(i,(200,200),(400,400),(255,153,255),cv2.FILLED)
cv2.rectangle(i,(200,200),(400,400),(0,0,0),4)
cv2.rectangle(i,(225,250),(275,300),(25,0,51),cv2.FILLED)
cv2.rectangle(i,(325,250),(375,300),(25,0,51),cv2.FILLED)
i[325:400,275:325]=25,0,51
cv2.rectangle(i,(225,250),(275,300),(0,0,0),4)
cv2.rectangle(i,(325,250),(375,300),(0,0,0),4)
cv2.rectangle(i,(275,325),(325,400),(0,0,0),4)
cv2.circle(i,(310,365),1,(102,255,255),4)

cv2.circle(i,(120,120),30,(255,0,0),30)
cv2.circle(i,(50,120),30,(0,255,0),30) #bgr
cv2.circle(i,(75,50),30,(0,0,255),30)
cv2.putText(i,"OpenCV",(10,175),cv2.FONT_ITALIC,1,(0,0,0),4)
#img,topleft,bottomleft,topright,bottomleft
cv2.imshow("image",i)
cv2.waitKey(0)