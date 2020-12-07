"""Importing All Functional Kivy Classes"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.popup import Popup

"""Importing The Backend Classes"""
from Simulation import Simulation
from main import Aircraft

#Setting default application window size
Window.size = (1280,720)

#Declaring Current Simulation Class For Current Runtime
curr_simulation = Simulation()

class Intro_Screen(Screen):

    num_aircrafts = ObjectProperty(None)
    filename = ObjectProperty(None)


    def intro_enter(self):

        num_aircrafts = self.num_aircrafts.text
        filename = self.filename.text

        #printing to terminal
        print(f'Current Number Of Aircraft In Airspace {num_aircrafts} and the Terrain File Is: {filename}')


        #input validation 
        ic = self.integer_checker(int(num_aircrafts))
        fc = self.filename_checker(str(filename))


        if ic == 1:

            #If integer check returns integer "1" prompt invalid input popup

            intro_pop = Popup(title = "Invalid Input(s)",
                                content = Label(text = "Please fill in all input boxs with valid data", font_size = 18))
            intro_pop.open()
        
        if fc == 1:

            #If filename search returns integer "1" prompt invalid input popup

            intro_pop = Popup(title = "Invalid Input(s)",
                    content = Label(text = "Please fill in all input boxs with valid data", font_size = 18))
            intro_pop.open()

        else:

            #else (input is valid) switch screen to main screen and clear input boxs
            self.intro_clear()
            sm.current = "main"
            pass

    
    def integer_checker(self, num_aircrafts):
        #Parsing kivy textinput values into simulation class methods
        return curr_simulation.aircraft_num_checker(int(num_aircrafts))

    def filename_checker(self, filename):
        #error checking with simulation method
        return curr_simulation.get_filename(str(filename))

    def intro_clear(self):

        self.num_aircrafts = ""
        self.filename = ""

class Main_Screen(Screen):

    aircraft_name = ObjectProperty(None)
    aircraft_speed = ObjectProperty(None)
    aircraft_alt = ObjectProperty(None)
    aircraft_pos = ObjectProperty(None)
    aircraft_dir = ObjectProperty(None)

    def pass_aircraft(self):

        return curr_simulation.add_aircraft_kivy(
            self.aircraft_name.text,
            self.aircraft_speed.text,
            self.aircraft_alt.text,
            self.aircraft_pos.text,
            self.aircraft_dir.text
        )
    
    def main_enter(self):


        if self.pass_aircraft() == True:

            self.main_clear()
        
        else:

            intro_pop = Popup(title = "Invalid Input(s)",
                    content = Label(text = "Please fill in all input boxs with valid data", font_size = 18))
            intro_pop.open()


    def main_clear(self):

        self.aircraft_name.text = ""
        self.aircraft_speed.text = ""
        self.aircraft_alt.text = ""
        self.aircraft_pos.text = ""
        self.aircraft_dir.text = ""


class Window_Manager(ScreenManager):
    pass










#Load kivy design langauage file 

kv = Builder.load_file("my.kv")

# declare variable "sm" (screenmanager) to be used as the window manager

sm = Window_Manager()

# iterable list of screens 

screens = [Intro_Screen(name = "intro"), Main_Screen(name = "main")]

# appending all screens within screens list to be individual widgets

for screen in screens:
    sm.add_widget(screen)

# screen to show when runtime executes (landing screen)
sm.current = "main"




"""App Run Class"""
class MyApp(App):

    # builds and returns current screen held within variable "sm"
    def build(self):
        return sm


# if name is main then do the following (execution line)
if __name__ == "__main__":
    MyApp().run()