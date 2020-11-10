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
        self.avg_speed = 0
        self.height_array = None
        self.aircraft_height = None
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
            print("\n")
            alt = int(input("Enter Aircraft's Altitude: "))
            print("\n")
            speed = int(input("Enter Aircraft's Speed:  "))
            print("\n")
            x = int(input("Enter Aircraft's Starting x coordinate:  "))
            print("\n")
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
    
    def get_avg_speed(self):

        self.avg_speed = 0

        for aircraft in self.all_aircraft:

            self.avg_speed += int(aircraft.speed)
        
        self.avg_speed = (self.avg_speed / self.aircraft_count)

        return 

    def create_terrain(self):

        """Method Supports Plotting and Visual Plot of HGT Terrain file"""

        siz = os.path.getsize(self.fn)
        dimension = int(math.sqrt(siz/2))

        assert dimension*dimension*2 == siz, 'Invalid file size'

        self.height_array = np.fromfile(self.fn, np.dtype('>i2'), dimension*dimension).reshape((dimension, dimension))
        self.x, self.y = np.meshgrid(range(self.height_array.shape[0]), range(self.height_array.shape[1]))

    def run_simulation(self, hours):

        self.get_avg_speed()
        self.aircraft_height = self.height_array.copy()

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
                avg_speed = self.ax1.text2D(plot_x_dim, plot_y_dim - 0.10, "Average Aircraft Speed: " + str(self.avg_speed), transform = plt.gcf().transFigure, fontsize = 12)
                curr_aircraft = self.ax1.text2D(plot_x_dim, plot_y_dim - 0.15, "Current Aircraft: " + str(None), transform = plt.gcf().transFigure, fontsize = 12)
                break
            

            self.ax1.pause(0.5)

            for aircraft in self.all_aircraft:

                self.aircraft_height[aircraft.pos[0] + aircraft.speed][aircraft.pos[1] + aircraft.speed]



                
        


            

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


