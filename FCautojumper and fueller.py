#file written by Gorfgorf23
#all code is open to be modified or deleted or used at any will, no payment or any form of contribution is required
#just have fun
#file updated the 01/03/2021 at 0:25 AM GMT + 1

#importing the great library of knoledge know as youtube
import tkinter as tk
from tkinter import filedialog, Text, PhotoImage
import os
import csv
import pydirectinput
import pyautogui
import time
from tkinter import simpledialog
from pynput.keyboard import Key, Controller as MController
from pynput.mouse import Button, Controller
from PIL import Image, ImageTk
mouse = Controller()
keyboard = MController()
global current_system_name
current_system_name = "pls press button to update"
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


def addfile():
    '''returns the file that a user selects when the function is called'''
    filename = filedialog.askopenfilename(initialdir="/",title="select your CSV file which has been premodified",filetypes=(("executables","*.csv"),("all files", "*.*")))
    global file
    file = filename
    return filename
    print(filename)


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

#Making GUI
root = tk.Tk()
root.title("FC jumper 2000")

#it was in the tutorial so its here ok??
canvas = tk.Canvas(root , height = 800, width = 1000, bg = "#23C6BF")
canvas.pack()

#the white frame bcos why not
frame = tk.Frame(root , bg = "lightblue")
frame.place(relwidth =0.8, relheight = 0.8 , relx = 0.1, rely = 0.1)


#text fo title
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "SOTV FC jumper\npls read the tutorial\n")

#I HAVE FAILED AT THIS FUCK THISD SHIT IVE HAD ENOUGH DAY 2 FINISHED
#button to selct current system
#picker = tk.Button(frame, text = "please enter first system(current system)", bg ="black" , fg = "white" ,
#                   activebackground = "blue", command  = lambda:system_namer())
#picker.pack()

#texte to indicate current system
#current_system = tk.Text(root, height=2, width=30)
#current_system.pack()
#while run == 1:
#current_system.insert(tk.END, "current system is:",current_system_name)

#text to indicate warnign for develepment
warning = tk.Text(frame, height = 5, width= 60)
warning.pack()
warning.insert(tk.END,"Alpha version , this jumper is still under develepment, \nuse at your own risk\n")


#button to find the .csv file
openfile = tk.Button(frame,activebackground="blue", text ="find CSV file", padx=10, pady = 5,fg ="white", bg="#23C6BF" , command = lambda:addfile())
openfile.pack()

#button to launch the jumper macro
runjumper = tk.Button(frame,activebackground="blue",text = "Start jumping",height = 15, width = 60, padx = 10, pady = 5,fg = "black", bg = "red",
                      command = lambda:jumper(file))
#runjumper.pack(side="top")
runjumper.place(relx=0.5, rely=0.5, anchor='center')

#button to go boom
exitbutton = tk.Button(root, text = "Exit", activebackground = "blue", fg = "white" , bg = "red" ,command = lambda:root.destroy())
exitbutton.pack()

#finishing loop
root.mainloop()

















