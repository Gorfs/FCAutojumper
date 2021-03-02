#main file that starts everything
from GUI import make_GUI #no need for make GUI since next step is to make a GUI in EDMC
from GUI import install
import tkinter as tk

def plugin_start3(plugin_dir: str) -> str: # function stolen from other plugin slightly modified
   """
   Load this plugin into EDMC
   """
   install("pydirectinput")
   install("pyautogui")
   plugin_app()
   print(f"I am loaded! My plugin folder is {plugin_dir}")
   return "FCautoJumper"

def plugin_app(parent:tk.Frame): #stolen from other plugin slighly modified
    """
    Create the button in EDMC window
    """
    frame = tk.Frame(parent)

    file_finder = tk.Button(frame,text="find CSV file",justify=tk.RIGHT , command = addfile())
    start_jumper = tk.Button(frame, text="start jumping", justify=tk.LEFT , command = jumper())
    this.spacer = tk.Frame(frame)
    return frame

def plugin_stop() -> None: #stolen from other plugin slightly modified
    """
    EDMC is closing
    """
    stop()
    print("Farewell cruel world!")



