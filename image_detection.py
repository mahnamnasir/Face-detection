from turtle import shape
import cv2
# reading image if 0 its rgb if 1 its grey scale or black n white
#img = cv2.imread("D:\some working for nccs\Tasks\open cv\image.jpg",1)
# type conversion
#print(type(img))
#size of image
#print(img.shape)
# to show the image
#cv2.imshow("face",img)
# wait for user to press key
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# Creating casscadeclassifier object creation mentioning pre-defined model

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# image reading
    img=cv2.imread("1.jpeg")
# conversion of image to greyscale as opencv dont detect color images
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors=5)
#for building the rectangle against face
    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y) , (x+w,y+h) ,(3,255,8) ,3)
# image showing 
    cv2.imshow("Gray",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    