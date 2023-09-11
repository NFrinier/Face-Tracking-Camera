import socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,50)
servo.start(float(2+(90/18)))
time.sleep(1)
angle = 9
move = 2

bufferSize = 1024
msgfs = "server up..."
serverPort = 5560
serverip = "ipv4 ip address for network setup"
bytesToSend = msgfs.encode('utf-8')
RPIsocket = socket.socket(socket.AF_INET.socket.SOCK_DGRAM)
RPIsocket.bind((serverip,serverPort))
print('listening...')
while True:
	mesg, address = RPIsocket.recvfrom(bufferSize)
	mesg = mesg.decode('utf-8')
	print(mesg)
	if mesg == 'left' and angle > 1:
		angle -= move
		servo.ChangeDutyCycle(2 + (angle / 18))
	elif mesg == 'right' and angle < 180:
		angle += move
	else:
		pass