import cv2


from cv2 import imshow
# Dataset load
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Video Capture
cap = cv2.VideoCapture("video1.mp4")
while True:

    success,img = cap.read()
    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    facecorrdinates = face_cascade.detectMultiScale(grayimg)

    for x,y,w,h in facecorrdinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("hello",img)
    key = cv2.waitKey(1)
    if(key==81 or key==113):
        break
cap.release()


