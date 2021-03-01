#Module that contains all the function which control the game itself


import csv
import pydirectinput
import pyautogui
import time

global file
file = 0
filename = 0
run = 1
global counter

def jumper(file):
    '''looks into the csv file and automatically sets the route of the FC to the different systems
     when calling jumper please add the fime with the GUI'''
    csv1 = csv.DictReader(open(file))
    csv2 = csv.reader(open(file))
    counter = 1
    time.sleep(10) #time to hop into elite

    for dics in csv1:
             print("next jump to " , dics["System Name"])
             if counter > 1:
                def refueling():
                    '''function which determines if you need to refuel in the next system that you are jumping to '''
                    if dics["Restock Tritium"] == "Yes":
                        return True
                    else:
                        return False
            #opens the rigth main panel
                pydirectinput.keyDown('4')
                time.sleep(0.025)
                pydirectinput.keyUp('4')
                time.sleep(1)

            #selects thje fleet carrier thing
                pydirectinput.keyDown('space')
                time.sleep(0.025)
                pydirectinput.keyUp('space')
                time.sleep(1)

            #selects the nav panel in FC thing
                pydirectinput.press('s')
                time.sleep(1)

            #Goes into nav apnnel thing
                pydirectinput.press('space')
                time.sleep(1)

            #confirmationn of glaxy map opening sequence
                pydirectinput.press('space')
                time.sleep(3)

            #going to nav part of gal map
            #selecting bit with search bar
                pydirectinput.press("e")
                time.sleep(1)
                pydirectinput.moveTo(175, 250)#going to selctor of great maginificance
                pydirectinput.press('space')
                time.sleep(1)
                pyautogui.write(dics['System Name'] , interval=0.025)
                time.sleep(1)
                pydirectinput.press('enter')
                time.sleep(0.5)
                time.sleep(5)
            #going to select system thingy

            #pressing GO BUTTON
                pydirectinput.press("d")
                pydirectinput.press("a")
                pydirectinput.press("space")
                time.sleep(1)
                print('jump plotted succesfully')

            #backing out
                time.sleep(2)
                pydirectinput.press('backspace')
                time.sleep(2)
                pydirectinput.press('backspace')
                time.sleep(1260)
                refuel()
             else:
                counter += 1


def refuel():
    '''function that refuels the FC for 500 tritium, uses basic keys'''
        #go into right panel
    pydirectinput.press("4")
    time.sleep(1)
        #go to inventory tab
    for i in range (4):
        pydirectinput.press("e")
        #go into transfer tab
    pydirectinput.press("d")
    pydirectinput.press("space")
    pydirectinput.press("w")
        #select tritium as comodity
    for j in range(9):
        pydirectinput.press("s")
    pydirectinput.press("w")
    pydirectinput.press("w")
        #transfer tritium too cargo hold
    for k in range(dics["Fuel Used"]):
        pydirectinput.press("aq")
        #accept transfer
    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("d")
    pydirectinput.press("space")
        #backout of inventory
    pydirectinput.press("backspace")
        #go to main rigth panel screen
    for p in range(4):
        pydirectinput.press("q")
        #selects FC panel for future jumps
    pydirectinput.press("w")
    pydirectinput.press("w")
    pydirectinput.press("a")
        #backout
    pydirectinput.press("backspace")
        #got to carrier managment
    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("w")
    pydirectinput.press("space")
        #going to tritium depot and selecting
    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("space")
    pydirectinput.press("space")
    pydirectinput.press("w")
        #dropping off tritium used in depot
    for l in range(dics["Fuel Used"]):
        pydirectinput.press("d")
        #confirm drop off
    pydirectinput.press("space")
        #full backout
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")