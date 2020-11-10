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
        self.aircraft_count = 0
        self.height_array = None
        self.x = None
        self.y = None
        self.ax1 = None


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
        
        self.aircraft_count = 0

        for aircraft in self.all_aircraft:

            print("Aircraft " + str(self.aircraft_count) + ": " + "Name: ", aircraft.name + ", " + "Altitude: ", str(aircraft.alt) + ", " + "Speed: ", str(aircraft.speed) + ", " + "Position: ", str(aircraft.pos)) 
            self.aircraft_count += 1

        return

    def create_terrain(self):

        """Method Supports Plotting and Visual Plot of HGT Terrain file"""

        siz = os.path.getsize(self.fn)
        dimension = int(math.sqrt(siz/2))

        assert dimension*dimension*2 == siz, 'Invalid file size'

        self.height_array = np.fromfile(self.fn, np.dtype('>i2'), dimension*dimension).reshape((dimension, dimension))
        self.x, self.y = np.meshgrid(range(self.height_array.shape[0]), range(self.height_array.shape[1]))

    def run_simulation(self, hours):

        fig = plt.figure(figsize=(10, 5))
        fig.suptitle("Flight Simulation", fontsize = 12, fontweight= "bold")
        plot_x_dim = 0.6
        plot_y_dim = 0.8

        self.ax1 = fig.add_subplot(121, projection = '3d')

        for hr in range(1, hours + 1):

            while hr == 1:
                p = self.ax1.plot_surface(self.x, self.y, self.height_array, cmap = 'terrain')
                self.ax1.set_zlim(1500, 3500)
                self.ax1.set_xlabel("Latitude")
                self.ax1.set_ylabel("Lonitude")
                self.ax1.set_zlabel("Height (m)")
                fig.colorbar(p)
                plt.title('Terrain: ' + str(self.fn))
                aircraft_title = self.ax1.text2D(plot_x_dim, plot_y_dim, "Aircraft Status", transform = plt.gcf().transFigure, fontsize = 12, fontweight = 'bold')
                active_aircrafts = self.ax1.text2D(plot_x_dim, plot_y_dim - 0.05, "Aircraft In AirSpace: " + str(self.aircraft_count), transform = plt.gcf().transFigure, fontsize = 12)
                break


        return


if __name__ == "__main__":

    sim = Simulation('N42W114.hgt')

    num = int(input("Enter Amount Of Aircraft:  "))

    sim.get_filename()
    sim.add_aircraft(num + 1)
    sim.get_aircraft(num + 1)

    sim.create_terrain()
    sim.run_simulation(10)

    plt.show()


