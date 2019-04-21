from pynput.mouse import Button,Controller
import socket
import bs4
import time
import math

ip = '192.168.1.17'
port = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))
mouse = Controller()

def sensor_data():
    sauce = bs4.BeautifulSoup(str(data),'lxml')
    x = sauce.find('accelerometer1')
    X = int(float(x.text))
    y = sauce.find('accelerometer2')
    Y = int(float(y.text))
    print('X: ' + X)
    print('Y: ' + Y)
    single_click = sauce.find('lightintensity')
    mouse.move(-X*4,-Y*4)

    #left click
    if int(float(single_click.text)) <= 10:
        mouse.click(Button.left)
        mouse.release(Button.left)
        print("Left Click")
        
while True:
    data = sock.recvfrom(port)
    print ('XML data: ' + data)
    sensor_data()
    time.sleep(0.02)
