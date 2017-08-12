import time, cv2

cap = cv2.VideoCapture(0)

ret, img = cap.read()

name = "Temp/" + str(time.time()) + ".jpg"

cv2.imwrite(name, img) 

			
				

