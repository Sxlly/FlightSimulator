import matplotlib.pyplot as plt 
import numpy as np
import math
import time
import os
import sys

from main import Aircraft

plt.style.use("fivethirtyeight")

class Simulation():

    def __init__(self, fn):
        self.fn = str(fn)
        self.all_aircraft = []
        self.height_array = None

    def get_filename(self):

        try:
            with open(self.fn, 'rb') as f:
                pass
            return self.fn

        except FileNotFoundError:
            print("Inputted File Name Does not Exist")
            return
    
    def add_aircraft(self, num):

        for ii in range(1, num):

            name = str(input("Enter Aircraft " + str(ii) + "'s " + "name: "))
            alt = int(input("Enter Aircraft's Altitude: "))
            speed = int(input("Enter Aircraft's Speed:  "))
            x = int(input("Enter Aircraft's Starting x coordinate:  "))
            y = int(input("Enter Aircraft's Starting y coordinate:  "))
            pos = (x, y)
            obj_name = name

            obj_name = Aircraft(name, alt, speed, pos)

            self.all_aircraft.append(obj_name)

        return

    def get_aircraft(self, num):
        
        count = 1

        for aircraft in self.all_aircraft:

            print("Aircraft " + str(count) + ": " + "Name: ", aircraft.name + ", " + "Altitude: ", str(aircraft.alt) + ", " + "Speed: ", str(aircraft.speed) + ", " + "Position: ", str(aircraft.pos)) 
            count += 1

        return

    def plot_terrain(self):

        """Method Supports Plotting and Visual Plot of HGT Terrain file"""

        siz = os.path.getsize(self.fn)
        dimension = int(math.sqrt(siz/2))

        assert dimension*dimension*2 == siz, 'Invalid file size'

        self.height_array = np.fromfile(self.fn, np.dtype('>i2'), dimension*dimension).reshape((dimension, dimension))
        x, y = np.meshgrid(range(self.height_array.shape[0]), range(self.height_array.shape[1]))

        fig = plt.figure(figsize=(15, 6))
        fig.suptitle("Flight Simulation", fontsize = 12, fontweight= "bold")

        ax1 = fig.add_subplot(121, projection = '3d')
        p = ax1.plot_surface(x, y, self.height_array, cmap = 'terrain')
        ax1.set_zlim(1500, 3500)
        ax1.set_xlabel("Latitude")
        ax1.set_ylabel("Lonitude")
        ax1.set_zlabel("Height (m)")
        fig.colorbar(p)
        plt.title('Terrain: ' + str(self.fn))

        plt.show()

        return
    
    def flight_model(self, hours):

        flight_arr = self.height_array.copy()
        count = 1

        for aircraft in self.all_aircraft:

            for ts in range(1, hours):

                print("Aircraft" + str(count))
                print(flight_arr[aircraft.pos[0] + 1][aircraft.pos[1] + 1])

            count += 1


if __name__ == "__main__":

    sim = Simulation('N42W114.hgt')

    num = int(input("Enter Amount Of Aircraft:  "))

    sim.get_filename()
    sim.add_aircraft(num + 1)
    sim.get_aircraft(num + 1)

    sim.plot_terrain()
    sim.flight_model(10)


