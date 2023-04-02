import socket
import time
import bs4

from pynput.mouse import Button, Controller
from consts import PORT


IP = '192.168.1.17'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))
mouse = Controller()


def sensor_data() -> None:
    oldz = 9
    sauce = bs4.BeautifulSoup(data, 'lxml')
    accelerometers = {
        'accelerometer1': None,
        'accelerometer2': None,
        'accelerometer3': None
    }

    for accelerometer in accelerometers.keys():
        accelerometers[accelerometer] = int(
            float(sauce.find(accelerometer).text))
        print(f'{accelerometer}: {str(accelerometers[accelerometer])}')

    single_click = sauce.find('lightintensity')
    mouse.move(- int(accelerometers['accelerometer1']) * 6,
               accelerometers['accelerometer2'] * 6)

    if int(float(single_click.text)) <= 10:
        mouse.click(Button.left)
        mouse.release(Button.left)
        print("Left Click")

    if oldz > accelerometers['accelerometer3']:
        if oldz - accelerometers['accelerometer3'] > 2:
            mouse.click(Button.right)
            mouse.release(Button.right)
            print("Right Click")
    else:
        oldz = accelerometers['accelerometer3']


while True:
    rawdata = sock.recvfrom(PORT)
    data = str(rawdata)
    sensor_data()
    time.sleep(0)
