from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

for i in range(1000):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(0.5)
    print(i)
