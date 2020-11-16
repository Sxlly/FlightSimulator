import matplotlib.pyplot as plt 
import numpy as np
import math
import time
import os
import sys
from main import Aircraft

"""Passing Style Command To Matplotlib"""
plt.style.use("fivethirtyeight")

class Simulation():

    """Driver Class"""
    """Top Level Class **Inheritance == NULL**"""
    """Associating with: main.py>>Aircraft Object Class"""

    def __init__(self, fn):

        self.fn = str(fn) #passing given file name of dtype string to class variable
        self.all_aircraft = [] #names of all current aircraft in list form
        self.terrain_col_list = [] #all aircraft & terrain collisions in list form
        self.aircraft_col_list = [] #all aircraft & aircraft collisions in lsit form
        self.aircraft_count = 0 #total amount of aircraft in airspace 
        self.avg_speed = 0 #average speed of aircraft in airspace
        self.avg_alt = 0 #average altitude of aircraft in airspace
        self.height_array = None #hgt height array passed to class variable 
        self.aircraft_height = None #copy of hgt height array for flight model mechanics 
        self.x = None #current x coordinate 
        self.y = None #current y coordinate 
        self.ax1 = None #subplot axis 1


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

            print("Aircraft " + str(self.aircraft_count + 1) + ": " + "Name: ", aircraft.name + ", " + "Altitude: ", str(aircraft.alt) + ", " + "Speed: ", str(aircraft.speed) + ", " + "Position: ", str(aircraft.pos)) 
            self.aircraft_count += 1

        return
    
    def get_avg_speed(self):

        self.avg_speed = 0

        for aircraft in self.all_aircraft:

            self.avg_speed += int(aircraft.speed)
        
        self.avg_speed = (self.avg_speed / self.aircraft_count)

        return 
    
    def get_avg_alt(self):

        self.avg_alt = 0

        for aircraft in self.all_aircraft:

            self.avg_alt += int(aircraft.alt)
        
        self.avg_alt = (self.avg_alt / self.aircraft_count)

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
        self.get_avg_alt()
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
                avg_alt = self.ax1.text2D(plot_x_dim, plot_y_dim - 0.20, "Average Aircraft Altitude: " + str(self.avg_alt), transform = plt.gcf().transFigure, fontsize = 12)
                terrain_cols_text = self.ax1.text2D(plot_x_dim, plot_y_dim - 0.25, "Terrain Collision: ", transform = plt.gcf().transFigure, fontsize = 12, color = 'black')
                terrain_cols_boo = self.ax1.text2D(plot_x_dim + 0.15, plot_y_dim - 0.25, str(False), transform = plt.gcf().transFigure, fontsize = 12, color = 'green')
                curr_pos_aircraft = self.ax1.text2D(plot_x_dim + 0.20, plot_y_dim - 0.15, "Position: " + str(None), transform = plt.gcf().transFigure, fontsize = 12, color = 'black')

                for aircraft in self.all_aircraft:
                    
                    #Pre Setting X,Y Coordinates For Each Aircraft
                    curr_x = aircraft.pos[0]
                    curr_y = aircraft.pos[1]

                break
            

            for aircraft in self.all_aircraft:

                plt.pause(0.75)

                #Pre Setting X,Y Coordinates For Each Aircraft
                curr_x = aircraft.pos[0]
                curr_y = aircraft.pos[1]

                curr_y = curr_y + aircraft.speed
                curr_x = curr_x
                curr_pos = self.aircraft_height[curr_x][curr_y + aircraft.speed]

                if (aircraft.alt <= int(curr_pos)):

                    terrain_cols_boo.set_text(str(True))
                    terrain_cols_boo.set_color('red')

                    self.terrain_col_list.append([str(aircraft.name), str((curr_x, curr_y))])

                    pass

                curr_aircraft.set_text("Current Aircraft: " + str(aircraft.name))
                curr_pos_aircraft.set_text("Position: " + str((curr_x, curr_y)))




                

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

    print(sim.terrain_col_list)


