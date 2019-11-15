import numpy as np 
import cv2

pic = np.zeros((500,500,3), dtype = 'uint8')

#To draw a rectangle
#cv2.rectangle(pic,(0,0),(500,150),(123,200,98),3,lineType=8,shift=0)

#To draw a line
#cv2.line(pic, (250,0),(500,350), (0,0,255))

#To draw a circle
#cv2.circle(pic,(50,50), 50, (0,0,255))

#To add a text
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'Udemy',(100,100), font,3,(255,255,255),4,cv2.LINE_8)


cv2.imshow("dark",pic)

cv2.waitKey(0)
cv2.destroyAllWindows()