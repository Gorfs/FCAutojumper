# bob of the Fleet carrier automatic jumper for elite dangerous Horizons
import csv
import time

from macro import one_jump, refuel


class Jumper:
    def __init__(self):
        '''
        initialising some values
        '''
        self.title = "AUTOMATIC FC JUMPER"
        self.file = ""
        self.refuel_bol = False
        self.tritium_place = None
        self.version = "1.5.0"

    def first_menu(self):
        print("Hello there. I am Bob your Fleet Carrier auto-guidance computing system version {}".format(self.version))
        print("Lets start off with some basics, for me to work I need to be used on Elite Dangerous in horizons \n"
              "My guidance coordinates will not work with odyssey since it is broken", end="\n\n")
        print(
            "Now that we have become aquainted. I need to know where you want to go. So please give me the path to your route.csv file \n"
            "If you have anyquestions please refer to my user manual (README.md)", end="\n\n")
        self.file = str(input(""))

        try:
            with open(self.file, "r") as file:
                print("hmm ,all seems to be good CMDR.")
        except:
            print("ERROR, CMDR I can't open that file for some reason, shutting down")
            if input("Type A if you want to restart, press ENTER to shut down") == "A":
                self.first_menu()
            else:
                exit()

        print("Now that I have the route.csv file I need to know if you wish for me to refuel your FC on the way")
        print("This does require a ship with at least a 75 ton capacity \n")
        print('If you with to enable this please type \"True\" under, if not please type \'False\' CAPITALS INCLUDED')
        inn = input("")
        if inn == "True":
            self.refuel_bol = True

        if self.refuel_bol == True:
            print("You have selected the refuel capability")
            print(
                "To do this task I require the placement of tritium in your cargo hold, please refer to the user manual")
            self.tritium_place = int(input("Please enter tritium placement"))
        else:
            print("You have selected to not use the refuel capabilities")

        print("\n It seems we have configured everything CMDR. I will start to jump on your command")
        input("Press Enter to start the jump (any button will do really)")
        self.jump()

    def jump(self):
        with open(self.file, "r") as file:
            csv1 = csv.DictReader(file)
            for dictionary in csv1:
                if dictionary["Fuel Used"] == 0:  # First jump and thus is wrong since we are already in system
                    pass
                else:
                    one_jump(dictionary["System Name"])
                    if self.refuel_bol:
                        refuel(dictionary["Fuel Used"], self.tritium_place)
                    print("jumping Process for {} was a success waiting for coolDown".format(dictionary["System Name"]))

            for i in range(20):
                print("{} minutes waited".format(i))
                time.sleep(60)


Jumper = Jumper()
Jumper.first_menu()
