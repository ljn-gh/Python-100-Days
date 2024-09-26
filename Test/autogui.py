import pyautogui

def mouse():
    x = pyautogui.size().width/2
    y = pyautogui.size().height/2
    ##screen = pyautogui.locateOnScreen()
    # print(pyautogui.size().width)
    # pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)
    ## pyautogui.move(pyautogui.size().width / 2, pyautogui.size().height / 2)
    #pyautogui.click(button='right')

    # pyautogui.dragTo(x,y,duration=0.2)

def keyboard():
    #pyautogui.press('a')
    pyautogui.typewrite('hello world')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')

def screenShot():
    screenshot = pyautogui.screenshot()
    screenshot.show()

def locateImg():
    img = '2024-08-06_10-13-48.png'
    screen = pyautogui.locateOnScreen(img)
    pyautogui.moveTo(screen.left+screen.width/2,screen.top+screen.height/2)
    print(screen)

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    #keyboard()
    #screenShot()
    #mouse()
    locateImg()
