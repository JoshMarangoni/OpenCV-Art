import numpy as np
import cv2

red = (0,0,255)
black = (0,0,0)
green = (0,255,0)

canvas = np.zeros((300,300,3), dtype="uint8")

for y in range(0,300,5):
	for x in range(0,300,10):
		if y%2==0:
			box1 = red
			box2 = black
		else:
			box1 = black
			box2 = red
		cv2.rectangle(canvas, (y,x), (y+5,x+5), box1, -1)
		cv2.rectangle(canvas, (y,x+5), (y+5,x+10), box2, -1)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.circle(canvas, (centerX,centerY), 35, green, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
