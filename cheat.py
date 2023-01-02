import os
import pyperclip as pc
from pynput.keyboard import Key, Listener
import pyautogui as pg
import pytesseract
from PIL import Image
import pyperclip as pc

var = os.popen('xsel').read()

while True:
    var1 = os.popen('xsel').read()
    if var != var1:
        pc.copy(var1)
        var = var1
        with open('index.txt','w') as f:
            f.write(f'<a href="https://www.google.com/search?q={var}" target="blank">{var}</a>\n')
        print(var)

# def copy(h):
#     try:
#         if h.char=="g":
#             img = pg.screenshot()
#             img.save('img.png')
#             text = pytesseract.image_to_string(Image.open('img.png'), lang='eng')
#             pc.copy(text)
#             print("hello")
#     except:
#         pass

# with Listener(on_press=copy) as l:
#     l.join()
