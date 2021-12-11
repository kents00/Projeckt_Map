import noise
import numpy as np
import random
import math

class BaseColor:
    # sets up the rgb base 
    # 0 -> 255
    r = 0.0
    g = 0.0
    b = 0.0
    a = 1.0

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = 1

    def GetTuple(self):
        return int(self.r), int(self.g), int(self.b)

    def SetColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def Copy(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b

    def SetWhite(self):
        self.SetColor(1, 1, 1)

    def SetBlack(self):
        self.SetColor(0, 0, 0)

    def SetColorFromGrayscale(self, f=0.0):
        self.SetColor(f, f, f)

class GenerateMap:

    def __init__(self, size=(50, 50), color_range=10, color_perlin_scale=0.025, scale=350, octaves=10, persistance=0.6,
                 lacunarity=3.0, x_starting_pos=0, y_starting_pos=0, threshold=-0.09):
        self.scale = scale
        self.octaves = octaves
        self.persistance = persistance
        self.lacunarity = lacunarity

        self.x_starting_pos=x_starting_pos
        self.y_starting_pos=y_starting_pos

        self.mapSize = size  # size in pixels
        self.mapCenter = (self.mapSize[0] / 2, self.mapSize[1] / 2)

        self.heightMap = np.zeros(self.mapSize)
        # self.colorMap = [[Color() for j in range(self.mapSize)] for i in range(self.mapSize)]

        self.randomColorRange = color_range
        self.colorPerlinScale = color_perlin_scale
        
        # you can setup your own map
        self.darkgrass = [90, 100, 35]
        self.meduimgrass = [117, 117, 47]
        self.lightgrass = [145, 135, 60]
        self.sand = [210, 200, 160]
        self.denseforest = [255, 0, 0]
        self.densetressandgrass = [127, 0, 0]
        self.graveldirt = [140, 70, 15]
        self.dirt = [120, 70, 20]
        self.tressandgrass= [64, 0, 0]
        self.maingrasslesstress = [0, 128, 0]
        self.longgrass = [0, 255, 0]

        self.threshold = threshold

    def return_initial_blank_map(self):
        return self.heightMap

    def get_map_corners(self):
        nw = self.heightMap[0][0]
        ne = self.heightMap[0][len(self.heightMap[0])-1]
        sw = self.heightMap[len(self.heightMap)-1][0]
        se = self.heightMap[len(self.heightMap)-1][len(self.heightMap[0])-1]
        return nw, ne, sw, se

    def get_map_start_position(self, start_position):
        pass

    def generate_map(self, map_type=""):
        random_nr = random.randint(0, self.mapSize[0])
        random_nr = 5
        for i in range(self.mapSize[0]):
            for j in range(self.mapSize[1]):

                new_i=i+self.y_starting_pos
                new_j=j+self.x_starting_pos


                self.heightMap[i][j] = noise.pnoise3(new_i / self.scale, new_j / self.scale, random_nr, octaves=self.octaves,
                                                     persistence=self.persistance, lacunarity=self.lacunarity,
                                                     repeatx=10000000, repeaty=10000000, base=0)
        print("Monocrhome map created")

        if map_type == "Generate" :
            gradient = self.heightMap
            color_map = self.add_color(gradient)
        else:
            color_map = self.add_color(self.heightMap)
        return color_map

    def add_color(self, world):
        color_world = np.zeros(world.shape + (3,))
        # print(color_world)
        for i in range(self.mapSize[0]):
            for j in range(self.mapSize[1]):
                
                # Genarating the threshold per color
                if world[i][j] < self.threshold + 0.070:
                    color_world[i][j] = self.darkgrass
                elif world[i][j] < self.threshold + 0.06:
                    color_world[i][j] = self.meduimgrass
                elif world[i][j] < self.threshold + 0.09:
                    color_world[i][j] = self.lightgrass
                elif world[i][j] < self.threshold + 0.090:
                    color_world[i][j] = self.dirt
                elif world[i][j] < self.threshold + 0.1:
                    color_world[i][j] = self.longgrass
                elif world[i][j] < self.threshold + 0.2:
                    color_world[i][j] = self.tressandgrass
                elif world[i][j] < self.threshold + 0.4:
                    color_world[i][j] = self.denseforest
                elif world[i][j] < self.threshold + 0.9:
                    color_world[i][j] = self.maingrasslesstress 
        print("Color map created")
        return color_world

    def apply_gradient_noise(self, world, c_grad):
        world_noise = np.zeros_like(world)

        for i in range(self.mapSize[0]):
            for j in range(self.mapSize[1]):
                world_noise[i][j] = (world[i][j] * c_grad[i][j])
                if world_noise[i][j] > 0:
                    world_noise[i][j] *= 50

        # get it between 0 and 1
        max_grad = np.max(world_noise)
        world_noise = world_noise / max_grad
        return world_noise

Paper_Color = (145, 135, 60)
Vegetation = (0, 128, 0)

def random_seed():
    seed = random.randint(0, 1000)
    return seed 
