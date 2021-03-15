import csv
import pydirectinput
import pyautogui
import time
import tkinter as tk
from tkinter import *

    #initialising the global and normal variables
global file
file = 0
filename = 0
run = 1
global counter
global placement
placement = 2
    #returning the name of the plugin to EDMC
PLUGIN_NAME = "JUMPER by gorfgorf"

def addfile()->str:
        '''
        returns the file that a user selects when the function is called
        file name should be a string
        no arguments needed
        '''
        print("addfile function called, olease find your file in the directory screen called")
        filename = filedialog.askopenfilename(initialdir="/",title="select your CSV file which has been premodified",filetypes=(("executables","*.csv"),("all files", "*.*")))
        global file
        file = filename
        return filename


class jumper:
    
    def __init__(self) -> None:
        """[returns none in class]

        Returns:
            [None]: [It was in the example code]
        """
        return None
    
    
    def on_load(self) -> str:
        """[returns the programes name to EDMC on load]

        Returns:
            str: [returns the name of the plugin to be loaded as the name of the plugin in the EDMC plugin section]
        """
        return PLUGIN_NAME

    
    def setup_main_ui(self, parent: tk.Frame):
        '''
        sets up the main UI in EDMC and initialises the functions that are needed
        '''       
        frame = tk.Frame(parent)
        
        T = tk.Text(frame, height=2, width=30)
        T.pack()
        T.insert(tk.END, "FC jumper\npls read the tutorial\n")
        
         
        openfile = tk.Button(frame, activebackground="blue", text="find CSV file", padx=10, pady=5, fg="white",
                         bg="#23C6BF", command=lambda: addfile())
        openfile.pack()
        
        def tritium_getter():
            global placement
            placement = int(Trit.get("1.0", END))

            #button to launch the macro :)
        runjumper = tk.Button(frame, activebackground="blue", text="Start jumping", padx=10, pady=5,
                          fg="black", bg="red",
                          command=lambda: jumper(file))
        runjumper.place(relx=0.5, rely=0.5, anchor='center')
        
            #Button the get the value in the text box
        tritiumplacer = tk.Button(frame, activebackground="blue", text="pls select tritium placement",  padx=10, pady=5,
                        fg="black", bg="#23C6BF",
                        command=lambda: tritium_getter())
        tritiumplacer.pack()  
        
            #text for the insertion of the amount of Ws required to select tritium
        Trit = tk.Text(frame, height=2, width=30)
        Trit.pack()
        Trit.insert(tk.END, "please replace this text with amount of time you press W to select tritium")
        
        def refuel():
                """
                [function that when called, uses a macro to refuel the carrier]
                """
                # go into right panel
                print("opening rigth panel ")
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
                for z in range(placement):
                    pydirectinput.press("w")
                # transfer tritium too cargo hold
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
                # go to main rigth panel screen
                print("going back to main panel to reset FC choice")
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
                print("going to carrier management")
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
                print("dropping off tritium in tritium depot")
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
        
        def jumper(file):
            '''
            looks into the csv file and automatically sets the route of the FC to the different systems
            when calling jumper please add the fime with the GUI
            '''
            print("Function jumper() has been called, Please make sure you have selected a .csv file before continuing.")
            print("The program will start soon")
            print("importing code things:")
            print("binary code is:110001010110000100100")
            time.sleep(3)
            print("importing complete")
            csv1 = csv.DictReader(open(file))
            print("CSV file found, good job")
            csv2 = csv.reader(open(file))
            counter = 1
            print("")
            print("You now have 10 seconds to go into your Elite before the code starts,")
            time.sleep(10) #time to hop into elite
            for dics in csv1:
                    print("next jump to " , dics["System Name"])
                    time.sleep(1)
                    if counter > 1:
                    #opens the rigth main panel
                        print("opening rigth panel ")
                        pydirectinput.keyDown('4')
                        time.sleep(0.025)
                        pydirectinput.keyUp('4')
                        time.sleep(1)

            #selects thje fleet carrier thing
                        print("going to FC section")
                        pydirectinput.keyDown('space')
                        time.sleep(0.025)
                        pydirectinput.keyUp('space')
                        time.sleep(1)

        #selects the nav panel in FC thing
                        print("going to nav section in FC directory")
                        pydirectinput.press('s')
                        time.sleep(1)

        #Goes into nav apnnel thing
                        print("entering nav section")
                        pydirectinput.press('space')
                        time.sleep(1)

        #confirmationn of glaxy map opening sequence
                        print("opening galaxy map")
                        pydirectinput.press('space')
                        time.sleep(3)

        #going to nav part of gal map
        #selecting bit with search bar
                        print("going to nav bar")
                        pydirectinput.press("e")
                        time.sleep(1)
                        pydirectinput.moveTo(175, 250)#going to selctor of great maginificance
                        pydirectinput.press('space')
                        time.sleep(1)
                        print("inputting system name in search bar")
                        pyautogui.write(dics['System Name'] , interval=0.025)
                        time.sleep(1)
                        print("goign to system in galaxy map")
                        pydirectinput.press('enter')
                        time.sleep(0.5)
                        time.sleep(5)
        #going to select system thingy

        #pressing GO BUTTON
                        print("pressing go button")
                        pydirectinput.press("d")
                        pydirectinput.press("a")
                        pydirectinput.press("space")
                        time.sleep(1)
                        print('jump plotted succesfully')

        #backing out
                        print("backing out")
                        time.sleep(2)
                        pydirectinput.press('backspace')
                        time.sleep(2)
                        pydirectinput.press('backspace')
                        print("waiting for 20 mins for cooldown")
                        counter2 = 0
                        for x in range(20):
                            print(counter2, "minutes waited")
                            counter2+=1
                            time.sleep(60)
                        print("10 seconds left before refuel")
                        time.sleep(10)
                        print("importing refuel() function")
                        jumper.refuel()
                    else:
                        counter += 1
          
    
          
        return frame

cc = jumper()

def plugin_start3(plugin_dir: str) -> str:
    return cc.on_load()

def plugin_app(parent: tk.Frame):
    return cc.setup_main_ui(parent)