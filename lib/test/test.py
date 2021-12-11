import sys, os
sys.path.append('../')
from vegetation import GenerateMap, random_seed 
from PIL import Image
import random
import uuid

class Basemap:
    def __init__(self, Menu="", generate_map=""):
        self.Menu (Menu)
        self.generate_basemap(generate_map)

    def generate_basemap(self, map_type=""):
        self.dark = (90, 100, 35)
        self.meduim = (117, 177, 47)
        self.light = (145, 135, 60)
        self.sand = (210, 200,160)

        if map_type == "basemap":
            print("\n\033[32;1mCreating Base Image\033[0m \nPlease select a number below \n\033[32;1m1.\033[0m Dark green \033[32;1m2.\033[0m Medium green \033[32;1m3.\033[0m Light green \033[32;1m4.\033[0m Light white")
            select = input(">")
            if select == "1":
                base_image = Image.new('RGB', (self.width, self.height), color=self.dark)
                base_image.save('output/' + str(uuid.uuid4()) + '.png')
                print("\n\033[32;1mDark green created\033[0m")
            elif select == "2":
                base_image = Image.new('RGB', (self.width, self.height), color=self.meduim)
                base_image.save('output/' + str(uuid.uuid4()) + '.png')
                print("\n\033[32;1mMeduim green created\033[0m")
            elif select == "3":
                base_image = Image.new('RGB', (self.width, self.height), color=self.light)
                base_image.save('output/' + str(uuid.uuid4()) + '.png')
                print("\n\033[32;1mLight green created\033[0m")
            elif select == "4":
                base_image = Image.new('RGB', (self.width, self.height), color=self.sand)
                base_image.save('output/' + str(uuid.uuid4()) + '.png')
                print("\n\033[32;1mLight white created\033[0m")
            else:
                print("Invalid input")
        else:
            print("Map type not found")

    def Menu(self, generate=""):
        print("""

    /$$$$$$$                                             /$$         /$$           /$$      /$$                    
    | $$__  $$                                           | $$        | $$          | $$$    /$$$                    
    | $$  \ $$ /$$$$$$   /$$$$$$  /$$  /$$$$$$   /$$$$$$$| $$   /$$ /$$$$$$        | $$$$  /$$$$  /$$$$$$   /$$$$$$ 
    | $$$$$$$//$$__  $$ /$$__  $$|__/ /$$__  $$ /$$_____/| $$  /$$/|_  $$_/        | $$ $$/$$ $$ |____  $$ /$$__  $$
    | $$____/| $$  \__/| $$  \ $$ /$$| $$$$$$$$| $$      | $$$$$$/   | $$          | $$  $$$| $$  /$$$$$$$| $$  \ $$
    | $$     | $$      | $$  | $$| $$| $$_____/| $$      | $$_  $$   | $$ /$$      | $$\  $ | $$ /$$__  $$| $$  | $$
    | $$     | $$      |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$  |  $$$$/      | $$ \/  | $$|  $$$$$$$| $$$$$$$/
    |__/     |__/       \______/ | $$ \_______/ \_______/|__/  \__/   \___/        |__/     |__/ \_______/| $$____/ 
                            /$$  | $$                                                                     | $$      
                           |  $$$$$$/                                                                     | $$      
                            \______/                                                                      |__/      
    """)
        if generate == "generate":
            self.height = int(input("\033[32;1mEnter the height of the map: \033[0m"))
            self.width = int(input("\033[32;1mEnter the width of the map: \033[0m"))
            map_data = GenerateMap((self.height, self.width), x_starting_pos=random_seed(), y_starting_pos=random_seed())
            mono_map = map_data.generate_map("Generate")
            Image.fromarray((mono_map).astype('uint8')).save('output/' + str(uuid.uuid4()) + '.png')
            print("\033[32;1mMap generated\033[0m")
        else:
            print("\033[32;1mSelect a number below \033[0m")
            print("\033[32;1m1. Generate map \033[0m")
            print("\033[32;1m2. Exit\033[0m")
            select = input(">")
            if select == "1":
                self.Menu("generate")
            elif select == "2":
                print("\033[32;1mExiting\033[0m")
                sys.exit()
            else:
                print("\033[32;1mInvalid input\033[0m")
                self.Menu("generate")
Basemap("generate", "basemap")
    
