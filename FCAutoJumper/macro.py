# this file contains 2 macros for jumping the Fleet carrier in elite dangerous

import pyautogui
import pydirectinput
import time


def one_jump(system: str) -> None:
    '''
        input -> name of the system you are meant to jump to
        output -> terminal text and keyboard strokes
        desc -> takes the name of a system in the galaxy and uses
                pyautogui to navigate through the menus to plot a jump to that system
                does not contain any checks though, effectively operating blind

        required modules ->  pyautogui, pydirectinput, time
    '''
    print("next jump to {}".format(system))
    # opens the right main panel
    pydirectinput.keyDown('4')
    time.sleep(0.025)
    pydirectinput.keyUp('4')
    time.sleep(1)

    # selects the fleet carrier thing
    pydirectinput.keyDown('space')
    time.sleep(0.025)
    pydirectinput.keyUp('space')
    time.sleep(10)

    # selects the nav panel in FC thing
    pydirectinput.press('s')
    time.sleep(1)

    # Goes into nav panel thing
    pydirectinput.press('space')
    time.sleep(1)

    # confirmation of galaxy map opening sequence
    pydirectinput.press('space')
    time.sleep(3)

    # going to nav part of gal map
    # selecting with search bar
    pydirectinput.press("up")
    time.sleep(1)
    pydirectinput.moveTo(175, 250)  # going to selctor of great maginificance
    pydirectinput.press('space')
    time.sleep(1)
    pyautogui.write(system, interval=0.025)
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(0.5)
    time.sleep(5)
    # going to select system thingy

    # pressing GO BUTTON
    pydirectinput.press("d")
    pydirectinput.press("a")
    pydirectinput.keyDown("space")
    time.sleep(3)
    pydirectinput.keyUp("space")
    time.sleep(1)
    print('jump plotted succesfully')

    # backing out
    time.sleep(10)
    pydirectinput.press('backspace')
    time.sleep(2)
    pydirectinput.press('backspace')
    print('end of the one_jump function')


def refuel(amount: int, tritium_placement: int) -> None:
    '''
    input -> int containing amount of tritium to refuel
    output -> terminal text and keyboard strokes
    desc -> uses keyboard inputs to simulate taking
    '''
    
    # got to carrier managment
    print("going to carrier management")
    pydirectinput.press("space")
    time.sleep(5) 
    # going to tritium depot and selecting
    print("going to tritium depot and selecting")
    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("space")
    pydirectinput.press("space")
    pydirectinput.press("w")
    # dropping off tritium used in depot
    print("dropping off tritium in tritium depot")
    # max amount of tritium is already preselected
    pydirectinput.press("space")
    # full backout
    print("fully backing out")
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")
    time.sleep(2)
    
    # go into right panelw
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
    for j in range(50):
        time.sleep(0.25)
        pydirectinput.press("s")
    print("selecting tritium as commodity")

    for z in range(tritium_placement):
        pydirectinput.press("w")
    # transfer tritium to cargo hold

    print("transferring tritium used by last jump")
    print("transfering: " + str(amount))
    pydirectinput.keyDown('a')
    time.sleep(10)
    pydirectinput.keyUp('a')
    # accept transfer
    print("accepting transfer")

    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("d")
    pydirectinput.press("space")
    time.sleep(2)

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
    pydirectinput.press("s")
    time.sleep(0.025)
    pydirectinput.press("d")
    time.sleep(1)

    # backout
    print("backing out")
    pydirectinput.press("backspace")

    # got to carrier managment
    print("going to carrier management")
    pydirectinput.press("space")
    time.sleep(5) 
    # going to tritium depot and selecting
    print("going to tritium depot and selecting")
    pydirectinput.press("s")
    pydirectinput.press("s")
    pydirectinput.press("space")
    pydirectinput.press("space")
    pydirectinput.press("w")
    # dropping off tritium used in depot
    print("dropping off tritium in tritium depot")
    # max amount of tritium is already preselected
    pydirectinput.press("space")
    # full backout
    print("fully backing out")
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")
    pydirectinput.press("backspace")
    time.sleep(2)
