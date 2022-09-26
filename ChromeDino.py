import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for x in range(100,110):
        for y in range(120,130):
            data[x, y]
    
    if data[x, y] < 100:
        for i in range(180,420): #(460,550)
            for j in range(410,475): #(230,265)
                if data[i, j] > data[x, y]:
                    hit("up")
                    return
        return

    if data[x, y] > 100:
        for i in range(180,440): #(460,570)
            for j in range(410,475): #(230,265)
                if data[i, j] < data[x, y]:
                    hit("up")
                    return
        return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 10 seconds")
    time.sleep(1)
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    print("The game is about to start")

   
# hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
        # Draw the rectangle for cactus
        # for i in range(180,390):
        #     for j in range(410,475):
        #         data[i, j] = 0
        
        # Draw the rectangle for birds
        # for x in range(100,110):
        #     for y in range(120,130):
        #         data[x, y] = 0

        # image.show()
        # break