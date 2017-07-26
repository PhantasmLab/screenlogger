#! /usr/bin/python
from pynput import mouse
from datetime import *
from zipfile import *
import pyautogui, os


__author__  = '_CYRAX_'
__copyright__ = 'Copyright 2017, łαbørαŧøriø Ŧαηŧαsмα'

__license__ = 'GPL'
__version__ = 'alpha 1.0.1'
__contact__ = 'Telegram : @cyr4x'

class MyException(Exception): pass

def on_click(x, y, button, pressed):

    if button == mouse.Button.left:
        raise MyException(button)

    if button == mouse.Button.right:
        raise MyException(button)


def compress(file, file_name):
    
    zip_arquive = ZipFile(file_name, 'a')
    zip_arquive.write(file)
    zip_arquive.close()


img_list = []
file_name = '{}.zip'.format(datetime.now().strftime('log-%a %b %d %Y')) #save .zip (change if you want but make sure that file .zip and .png stay into same directoty to avoid issues)

while 1:
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            click = str(e)

    try:
        if click == 'Button.left' or 'Button.right':
            scr1 = pyautogui.screenshot()
            png_file = '{}.png'.format(datetime.now().strftime('%c'))
            scr1.save(png_file) #save img
            img_list.append(png_file)

            
            if len(img_list) == 5: #amount of img to compact (you can change if you want to)
                for imagen in img_list:
                    compress(imagen, file_name)
            
                
                for img in img_list: #after the compressed the file img will be deleted
                    os.remove(img)
                img_list.clear()
        
    except:
        pass
