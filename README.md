# BOB, your FC Pilot.

## Intro

Bob, is your fleet carrier auto-pilot, he can take over for you on long distance trips, and he'll do it for free.

bob is completely open source and open to everybody, you can feel free to fork this repository and change bob in any way you see fit.

### summary

1. intro
2. disclaimer
3. requirements
4. How it works
5. Installing/Using Bob
6. Contacting me
7. End Notes

## Disclaimer

bob is a macro and is considered SCRIPTING, and is bannable / punishable by Fdev. I am not responsible for anyone getting banned or loosing FC privledges for using bob.
Use him at your own risk.

## Requirements

Bob is based in Python 3.9 and uses "pyautogui" and "pydirectinput".
To use bob you will need to install python and these packages.
There is a .exe file included but it is very unstable and is more than likely to break.

Bob must be used in elite dangerous Horizons, since the macros are made for those menus,

You must have the default keybinds for keyboard and mouse for bob to access them.

Elite must be open and the main focused application at all times for bob to work.

## How it works

All bob does is act like you, it presses "virtual keys" on a keyboard and that interacts with your currently open application. In Elite you can use this macro to interact with menus and thus do stuff with your fleet carrier.

## Installing/Using Bob

1. Download this git repository by pressing on "code" (top right of this main page) and Download as .zip.

2. unzip the downloaded folder somewhere you will remember it.
3. Go to https://www.spansh.co.uk/fleet-carrier and input the data of your next trip, be sure to be precise about everything as a mistake can be the difference between being stranded in deep space and your destination
4. Once it is done "calculating" click "Download as CSV"
5. Move that downloded CSV file to your Desktop
6. Right click on your csv file and select it's path, it should look like
   ```
   C:\Desktop\
   ```
7. open up a text editor and copy your reference on it and add the name of you file on the end, include the .csv, like this:
   ```
   C:\Desktop\route.csv
   ```
8. launch up Elite dangerous and get on your carrier

9. (Skip this step if you are not planning on using refuelling)
   navigate to your fleet carrier's inventory screen and go all the way to the bottom.
   now press "up" until you have highlited tritium, The amount of times you have pressed "up" is what bob calls tritium count. Write that in your text-editor with your csv file reference
10. Now in your internal pannel (the pannel on the right side your of cmdr) highlight the FC section then press "exit" to leave it highlighted.

11. Almost there, double click on bob.py, and a terminal will appear, first he will ask you for your file reference so just copy that from your text-editior, then just follow the instruction in the terminal to continue.

12. Once you arrive at the end of configuration click any button to start the countdown, you have 10 seconds to focus your game on screen before bob starts working.
13. Now Bob should be taking you to your destination CMDR, Good luck out there.

## Contacting me

If there is an issue or you want some extra information you can contact me with this email:

```
archiebeales@gmail.com

or

archie.beales@etu.u-paris.fr
```

## End Notes

If you like this project and you have a github account please feel free to leave a star as it shows me that my work is actually useful.
o7.
