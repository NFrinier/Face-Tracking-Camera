import cv2 as cv
import socket
serverAddress = ('Server address in ipv4 config goes here... not giving away my ip that easy', 5560)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20)
    if len(faces_rect) > 0:
        x, y, w, h = faces_rect[0]

        #cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        x = int(x + w /2)
        if x < 360 and x > 290:
            msg = 'centered'
        elif x < 300:
            msg = 'right'
        else:
            msg = 'left'
        bts = msg.encode('utf-8')
        UDPClient.sendto(bts, serverAddress)

    cv.imshow('Watchmen', frame)
    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
