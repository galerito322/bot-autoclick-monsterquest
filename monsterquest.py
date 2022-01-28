from asyncio import sleep
#from pydoc import locate
import pyautogui as py
import time
import keyboard

def clickBtn(imgLocation):
    py.moveTo(imgLocation, duration=0.1)
    py.click()
    time.sleep(1)
    pass

def locateImg(img1, img2):
    print("\nSearching for image: ",img1,"or",img2)
    for i in range(10):
        time.sleep(1)
        imgLocationOne = py.locateOnScreen(img1, confidence= 0.8)
        imgLocationTwo = py.locateOnScreen(img2, confidence= 0.8)
        time.sleep(0.25)
        if imgLocationOne or imgLocationTwo != None:
            #print('\n',img1, 'Position:', imgLocationOne, '\n', img2, 'Position', imgLocationTwo)
            if imgLocationOne != None:
                print("\nImage:",img1,"found\n")
            if imgLocationTwo != None:
                print("\nImage:",img2,"found\n") 

            clickBtn(imgLocationOne or imgLocationTwo)
            py.moveTo(1200, 800) # posição aletória para afastar o mouse
            #time.sleep(0.2)
            break
        else:
            print(".", end='')

#define que o click sera sempre + 50 pixels no eixo x da img encontrada (isso faz com q o click acontece sempre na primeira carta)
def start(name): 
    py.scroll(-1500)
    print("\nSearching for fight buttons: ")
    while True:
        time.sleep(1)
        imgLocation = py.locateOnScreen(name, confidence= 0.85)
        if imgLocation != None:
            print("\nclicking in first card\n")
            #o valor passado para moveTo deve ser do tipo int, logo deve-se definir a posição[] do valor desejado da lista para x e y do moveTo()
            py.moveTo(imgLocation[0] + 50, imgLocation[1] + 10, duration= 0.2)
            #moveTo(x, y, width, height)
            py.click()
            #time.sleep(1)
            break   
        else:
            print(".", end='')
            
def main():
    start('buttons_fight.png')
    locateImg('skill_attack.png', 'attack.png')
    locateImg('ok.png', 'try_again.png')

input("Press enter to init")
time.sleep(2)
while True:
    main()


