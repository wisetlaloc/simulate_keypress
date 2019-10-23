from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

for i in range(100):
  for j in range(5):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(0.2)
  time.sleep(1)
  keyboard.press(Key.space)
  keyboard.release(Key.space)
  time.sleep(5)
  print(i)
