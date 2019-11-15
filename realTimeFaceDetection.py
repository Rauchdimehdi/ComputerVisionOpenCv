import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videoCapture = cv2.VideoCapture(0)
scale_factor = 1.3

while 1:
	ret,pic =videoCapture.read()
	faces = face_cascade.detectMultiScale(pic, scale_factor, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(pic, (x,y),(x+w, y+h),(255,0,0), 2)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(pic,'Me',(x,y), font, 2, (255,255,255),2, cv2.LINE_AA)

	print('Number of faces fount {}', format(len(faces)))
	cv2.imshow('face', pic)
	k= cv2.waitKey(30) & 0xff
	if k==2:
		break
cv2.destroyAllWindows()