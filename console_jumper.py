#started by gorfgorf23 on the 14/11/2021
# this is going to be a revision on my previous automatic Fleet carrier jumper that I made a while back, with the realease of odessey I want to remake it but with a twist, I don't want it to look like shit.

#this is given with the presumption you know what it does, THIS IS A GLORIFIED MACRO. IT TAKES NO INPUT FROM THE GAME

#If you jump somewhere that you didn't want to go because you weren't looking at it then it is your fault. I take no responsobility for the problem.

#this is going to be one big class with basically two type of methodes, the first being the macro methodes meant to interact with the game and the rest being the methodes to trigger / support the macros, so the gui and the rest.

#the first version of this the menu will be done in the console to make life easier.

import csv
from typing import Text
import pydirectinput
import pyautogui
import time
import os

class jumper():
    def __init__(self):
        self.title = "AUTOMATIC FC JUMPER" 
        self.current_info = "Stage 0 = launching program"
        self.file = ""
        self.refuel_bol = False
        self.tritium_place = None
    
    def first_menu(self):
        print("\n Hello there and welcome to the automatic Fleet Carrier jumper. \n All code written by gorfgorf23 \n ==========================\n \n")

        print("Step n1 you must find the .csv file that you downloaded and type it's location in the console.\n \n You must now select your file by typing in the path of you csv file into the console.")
        self.file = input("")
        if self.file.endswith('.csv') == False:
            print('\nthe file was not a csv file. please try again\n')
            self.first_menu()
        else:
            with open(self.file) as file:
                dics = csv.reader(file)

                print("\n All looks good for now, your file path should be " , self.file)
        print('Thanks for giving me the file location, next step is the refuel capabilities, Do you want to enable automatic refuelling of your Fleet carrier? \[1] for yes and [0] for no \n ==============')
        if int(input("")) == 1:
            self.refuel_bol = True
        else:
            self.refuel_bol = False
        
        print("/n thanks you have choosen" , self.refuel_bol , '\n \n ==================')
        if self.refuel_bol == True:
            print('Since you have chosen to have the refuel option as On then you must supply addition information known as the tritium placement. refer to README for more details on that. please give the number as input below this, thanks\n')
            self.tritium_place = int(input(""))
        
        self.launch_menu()

#We now have the .csv file path and the tritium placement on the carriere as well as if the client wants the auto refuelling.

    def launch_menu(self):
        print("=====================\n It would seem I now have all the informatino I need to launch the fleet carrier, for preflight checks make sure you have a 512 tons cutter which is completely empty on the deck of you fleet carrier. That all the menus are in their default places and that no destination is plotted.\n")
        print('\n Once you are ready to lift off just type in GO into the console and click on the game again. if you want to restart then enter[0]\n \n =======')
        if input("") == 'GO':
            self.Jump()
        else:
            print("error detected, exiting all. stopping all proccess")
            exit()
        
    def Jump(self):
        with open(self.file) as csv1:
            dics = csv.DictReader(csv1)
            def refuel():
                '''
                function that refuels the FC for 500 tritium, uses basic keys
                '''
                # go into right panel
                pydirectinput.press("4")
                time.sleep(1)
                # go to inventory tab
                print("going to inventory tab")
                for i in range(4):
                    pydirectinput.press("e")
                time.sleep(1)
                # go into transfer tab
                print("going to transfer tab")
                time.sleep(1)
                pydirectinput.press("d")
                pydirectinput.press("d")
                pydirectinput.press("d")
                pydirectinput.press("d")
                time.sleep(1)
                pydirectinput.press("space")
                pydirectinput.press("w")
                # select tritium as comodity
                for j in range(9):
                    time.sleep(0.25)
                    pydirectinput.press("s")
                print("selecting tritium as commodity")
                for z in range(self.tritium_place):
                    pydirectinput.press("w")
                # transfer tritium to cargo hold
                print("transfering tritium used by last jump")
                for k in range(int(dics["Fuel Used"])):
                    time.sleep(0.025)
                    pydirectinput.press("a")
                # accept transfer
                print("accepting transfer")
                pydirectinput.press("s")
                pydirectinput.press("s")
                pydirectinput.press("d")
                pydirectinput.press("space")
                # backout of inventory
                print("backing out of inventory")
                pydirectinput.press("backspace")
                # go to main right panel screen
                for p in range(4):
                    pydirectinput.press("q")
                    time.sleep(1)
                # selects FC panel for future jumps
                print("resseting FC panel for future jumps")
                time.sleep(2)
                pydirectinput.press("w")
                time.sleep(0.025)
                pydirectinput.press("w")
                time.sleep(0.025)
                pydirectinput.press("w")
                time.sleep(0.025)
                pydirectinput.press("w")
                time.sleep(0.025)
                pydirectinput.press("w")
                time.sleep(0.025)
                pydirectinput.press("w")
                time.sleep(1)
                pydirectinput.press("a")
                time.sleep(0.025)
                pydirectinput.press("a")
                time.sleep(0.025)
                pydirectinput.press("a")
                time.sleep(0.025)
                pydirectinput.press("a")
                time.sleep(1)
                pydirectinput.press("s")
                time.sleep(0.025)
                pydirectinput.press("d")
                time.sleep(1)
                # backout
                print("backing out")
                pydirectinput.press("backspace")
                # got to carrier managment
                self.add_to_info("going to carrier management")
                pydirectinput.press("s")
                pydirectinput.press("s")
                pydirectinput.press("w")
                pydirectinput.press("space")
                # going to tritium depot and selecting
                print("going to tritium depot and selecting")
                pydirectinput.press("s")
                pydirectinput.press("s")
                pydirectinput.press("space")
                pydirectinput.press("space")
                pydirectinput.press("w")
            # dropping off tritium used in depot
                self.add_to_info("dropping off tritium in tritium depot")
                for l in range(int(dics["Fuel Used"])):
                    pydirectinput.press("d")
                # confirm drop off
                    print("confirming dropoff")
                pydirectinput.press("space")
            # full backout
                print("fully backing out")
                pydirectinput.press("backspace")
                pydirectinput.press("backspace")
                pydirectinput.press("backspace")
            for dics in csv1:
                time.sleep(1)           
                # opens the right main panel
                print("opening rigth panel ")
                pydirectinput.keyDown('4')
                time.sleep(0.025)
                pydirectinput.keyUp('4')
                time.sleep(1)

        # selects the fleet carrier thing
                pydirectinput.keyDown('space')
                time.sleep(0.025)
                pydirectinput.keyUp('space')
                time.sleep(1)

    # selects the nav panel in FC thing
                print("going to nav section in FC directory")
                pydirectinput.press('s')
                time.sleep(1)

    # Goes into nav pannel thing
                print("entering nav section")
                pydirectinput.press('space')
                time.sleep(1)

    # confirmationn of glaxy map opening sequence
                print("opening galaxy map")
                pydirectinput.press('space')
                time.sleep(3)

    # going to nav part of gal map
    # selecting bit with search bar
                print("going to nav bar")
                pydirectinput.press("e")
                time.sleep(1)
                # going to selector of great maginificance
                pydirectinput.moveTo(175, 250)
                pydirectinput.press('space')
                time.sleep(1)
                print("inputting system name in search bar")
                pyautogui.write(dics['System Name'], interval=0.025)
                time.sleep(1)
                print("goign to system in galaxy map")
                pydirectinput.press('enter')
                time.sleep(0.5)
                time.sleep(5)
    # going to select system thingy

    # pressing GO BUTTON
                print("pressing go button")
                pydirectinput.press("d")
                pydirectinput.press("a")
                pydirectinput.press("space")
                time.sleep(1)
                time.sleep(6)

    # backing out
                pydirectinput.press('backspace')
                time.sleep(2)
                pydirectinput.press('backspace')
                counter2 = 0
                for x in range(20):
                    print(counter2, "minutes waited")
                    counter2 += 1
                    time.sleep(60)
                if self.refuel_bol == True:
                    print("10 seconds left before refuel")
                    time.sleep(10)
                    print("importing refuel() function")
                    refuel()

    def run(self):
        #runs stuff:
        self.first_menu()


jump = jumper()
jump.run()