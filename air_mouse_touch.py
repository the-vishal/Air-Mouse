import socket
import time
import re

from pynput.mouse import Button, Controller
from consts import PORT, PATTERN_CLICK, PATTERN_CURSOR, PATTERN_X, PATTERN_Y, \
    BASE_PATTERN


mouse = Controller()
s = socket.socket()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
s.bind((ip_address, PORT))


def mouse_action() -> None:
    match = re.search(PATTERN_CLICK, str(url))
    if match:
        print(match.group())
        if "Right" in match.group():
            mouse.click(Button.right)
        elif "Left" in match.group():
            mouse.click(Button.left)

    # Cursor
    match = re.search(PATTERN_CURSOR, str(url))
    if match:
        match_x = re.search(PATTERN_X, match.group())
        if match_x:
            x = re.search(fr"{BASE_PATTERN}", match_x.group())
            if x:
                print(x.group())

        match_y = re.search(PATTERN_Y, match.group())
        if match_y:
            y = re.search(fr"{BASE_PATTERN}", match_y.group())
            if y:
                print(y.group())
        mouse.position = (5 * int(x.group()), 3 * int(y.group()))


while True:
    s.listen(5)
    c, addr = s.accept()
    url = c.recv(4800)
    # print(url)
    mouse_action()
    time.sleep(0)
