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

"""Importing The Backend Classes"""
from Simulation import Simulation
from main import Aircraft


class MyLayout(Widget):

    num_aircrafts = ObjectProperty(None)
    filename = ObjectProperty(None)


    def press(self):

        num_aircrafts = self.num_aircrafts.text
        filename = self.filename.text

        #printing to terminal
        print(f'Current Number Of Aircraft In Airspace {num_aircrafts} and the Terrain File Is: {filename}')

        #Parsing kivy textinput values into simulation class methods
        Simulation.add_aircraft(int(num_aircrafts))

        #parsing filename into simualtion method
        Simulation.fn = str(filename)

        #error checking with simulation method
        Simulation.get_filename()

        

        #clear input boxs 
        self.num_aircrafts = ""
        self.filename = ""

"""App Run Class"""
class MyApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()