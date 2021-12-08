from PIL import Image
import numpy as np


class Basemap:
    def __init__(self, width, height, generate_map=""):
        self.width = width
        self.height = height
        self.generate_map(generate_map)

    def generate_map(self, map_type=""):
        self.dark = (90, 100, 35)
        self.meduim = (117, 177, 47)
        self.light = (145, 135, 60)
        self.sand = (210, 200,160)

        if map_type == "basemap":
            print("Creating base image \n Please select a number below \n 1. Dark grass  2. Medium Grass  3. Light Grass  4. Sand")
            select = input(">")
            if select == "1":
                base_image = Image.new('RGB', (self.width, self.height), color=self.dark)
                base_image.save("dark_grass.png")
                print("Dark grass created")
            elif select == "2":
                base_image = Image.new('RGB', (self.width, self.height), color=self.meduim)
                base_image.save("dark_grass.png")
                print("Dark grass created")
            elif select == "3":
                base_image = Image.new('RGB', (self.width, self.height), color=self.light)
                base_image.save("dark_grass.png")
                print("Dark grass created")
            elif select == "4":
                base_image = Image.new('RGB', (self.width, self.height), color=self.sand)
                base_image.save("dark_grass.png")
                print("Dark grass created")
            else:
                print("Invalid input")
        else:
            print("Map type not found")
        
height = int(input("Enter the height of the map: "))
width = int(input("Enter the width of the map: "))
map_type = input("Enter the type of map you want to create: ")

generate_amp = Basemap(width, height, generate_map=map_type)