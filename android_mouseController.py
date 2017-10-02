from pynput.mouse import Button,Controller
import socket
import bs4
import time
import math

ip = '192.168.43.173'
port = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))


mouse = Controller()

a = [0]
b = [0]

def sensor_data():

    sauce = bs4.BeautifulSoup(data,'lxml')
    x = sauce.find('accelerometer1')
    X = int(float(x.text))
    y = sauce.find('accelerometer2')
    Y = int(float(y.text))
    #z = sauce.find('accelerometer3')
    #Z = int(float(z.text))
    #print(X)
    #print(Y)
    #Pythagoras Theorem for 3rd axis
    #h1 = int(math.sqrt(X**2 + Z**2))
    #h2 = int(math.sqrt(Y**2 + Z**2))
    single_click = sauce.find('lightintensity')
    mouse.move(-X*4,-Y*4)
    
    #left click
    if int(float(single_click.text)) <= 10:
        mouse.click(Button.left)
        mouse.release(Button.left)
        #print("Right Click")

    #print(x.text)
    #print(y.text)

while True:
          data,addr = sock.recvfrom(4800)
          #print(data)
          sensor_data()
          time.sleep(0)


