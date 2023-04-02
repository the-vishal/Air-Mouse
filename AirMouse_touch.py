import socket
import time
import re

from pynput.mouse import Button, Controller


PATTERN_CLICK = r"n([\w]+)'"
PATTERN_CURSOR = r"X=([\b\w\D\.]+)'"
PATTERN_X = r"X=([\d]+)"
PATTERN_Y = r"Y=([\d]+)"
PORT = 5555


mouse = Controller()
s = socket.socket()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
s.bind((ip_address, PORT))


def mouse_Action() -> None:
    match = re.search(PATTERN_CLICK,str(url))
    if match:
        print(match.group())
        if "Right" in match.group():
            mouse.click(Button.right)
        elif "Left" in match.group():
            mouse.click(Button.left)

    #Cursor
    match2 = re.search(PATTERN_CURSOR,str(url))
    if match2:
        matchx = re.search(PATTERN_X,match2.group())
        if matchx:
            #print(matchx.group())
            patx = r"([\d]+)"
        x = re.search(patx, matchx.group())
        if x:
            print(x.group())

        matchy = re.search(PATTERN_Y,match2.group())
        if matchy:
            #print(matchy.group())
            paty = r"([\d]+)"
            y = re.search(paty,matchy.group())
            if y:
                print(y.group())
        mouse.position=(5*int(x.group()), 3*int(y.group()))


while True:
    s.listen(5)
    c, addr = s.accept()
    url = c.recv(4800)
    # print(url)
    mouse_Action()
    time.sleep(0)

