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
Window.size = (750,500)

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


        ic = self.integer_checker(int(num_aircrafts))
        fc = self.filename_checker(str(filename))


        if ic == 1:

            intro_pop = Popup(title = "Invalid Input(s)",
                                content = Label(text = "Please fill in all input boxs with valid data", font_size = 18))
            intro_pop.open()
        
        if fc == 1:

            intro_pop = Popup(title = "Invalid Input(s)",
                    content = Label(text = "Please fill in all input boxs with valid data", font_size = 18))
            intro_pop.open()

        else:
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

        Simulation.add_aircraft_kivy(
            str(self.aircraft_name.text),
            int(self.aircraft_speed.text),
            int(self.aircraft_alt.text),
            tuple(self.aircraft_pos.text),
            str(self.aircraft_dir.text)
        )
    
    def main_enter(self):

        self.pass_aircraft()

        self.aircraft_name.text = ""
        self.aircraft_speed.text = ""
        self.aircraft_alt.text = ""
        self.aircraft_pos.text = ""
        self.aircraft_dir.text = ""


class Window_Manager(ScreenManager):
    pass











sm = Window_Manager()

screens = [Intro_Screen(name = "intro"), Main_Screen(name = "main")]

for screen in screens:
    sm.add_widget(screen)

"""App Run Class"""
class MyApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        return Intro_Screen()

if __name__ == "__main__":
    MyApp().run()