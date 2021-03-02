#module containing the GUI functions used by the program
from Macro import jumper
import tkinter as tk
from tkinter import filedialog
import subprocess
import sys

def install(package):
    '''fucntion i stole of the internet. It is required to install the packages required for EDMC to install the "pyautogui" and "pydirectinput" modules
    also function that is making the error statement'''
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


global current_system_name
global file
file = 0
filename = 0
run = 1
global counter



def addfile():
    '''returns the file that a user selects when the function is called'''
    filename = filedialog.askopenfilename(initialdir="/",title="select your CSV file which has been premodified",filetypes=(("executables","*.csv"),("all files", "*.*")))
    global file
    file = filename
    return filename
    print(filename)

def make_GUI():
    # Making GUI
    root = tk.Tk()
    root.title("FC jumper 2000")

    # it was in the tutorial so its here ok??
    canvas = tk.Canvas(root, height=800, width=1000, bg="#23C6BF")
    canvas.pack()

    # the white frame bcos why not
    frame = tk.Frame(root, bg="lightblue")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # text fo title
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "SOTV FC jumper\npls read the tutorial\n")

    # I HAVE FAILED AT THIS FUCK THISD SHIT IVE HAD ENOUGH DAY 2 FINISHED
    # button to selct current system
    # picker = tk.Button(frame, text = "please enter first system(current system)", bg ="black" , fg = "white" ,
    #                   activebackground = "blue", command  = lambda:system_namer())
    # picker.pack()

    # texte to indicate current system
    # current_system = tk.Text(root, height=2, width=30)
    # current_system.pack()
    # while run == 1:
    # current_system.insert(tk.END, "current system is:",current_system_name)

    # text to indicate warnign for develepment
    warning = tk.Text(frame, height=5, width=60)
    warning.pack()
    warning.insert(tk.END, "Alpha version , this jumper is still under develepment, \nuse at your own risk\n")

    # button to find the .csv file
    openfile = tk.Button(frame, activebackground="blue", text="find CSV file", padx=10, pady=5, fg="white",
                         bg="#23C6BF", command=lambda: addfile())
    openfile.pack()

    # button to launch the jumper macro
    runjumper = tk.Button(frame, activebackground="blue", text="Start jumping", height=15, width=60, padx=10, pady=5,
                          fg="black", bg="red",
                          command=lambda: jumper(file))
    # runjumper.pack(side="top")
    runjumper.place(relx=0.5, rely=0.5, anchor='center')

    # button to go boom
    exitbutton = tk.Button(root, text="Exit", activebackground="blue", fg="white", bg="red",
                           command=lambda: exit())
    exitbutton.pack()

    # finishing loop
    root.mainloop()

