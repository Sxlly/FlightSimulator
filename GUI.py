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

from Simulation import Simulation
from main import Aircraft

class Create_Main_Window(Screen):
    n_aircrafts = ObjectProperty(None)
    height_file = ObjectProperty(None)

    def enter(self):
        if (self.n_aircrafts != 0 and self.height_file):
            Simulation.aircraft_count = int(self.n_aircrafts.text)
            Simulation.fn = self.height_file.text

            self.reset()

            sm.current = "Enter"
        
        else:
            invalid_aircraft()
    
    def enter(self):
        self.reset()
        sm.current = "Enter"
    
    def reset(self):
        self.n_aircrafts.text = ""
        self.height_file = ""

class Aircraft_Input_Window(Screen):

    name = ObjectProperty(None)
    alt = ObjectProperty(None)
    speed = ObjectProperty(None)
    pos = ObjectProperty(None)
    direction = ObjectProperty(None)

    def enter_aircraft_button(self):

        if Simulation.add_aircraft_kivy(self.name.text, int(self.alt.text), int(self.speed.text), tuple(self.pos.text), self.direction.text):

            Main_Window.current = self.name.text
            self.reset()
            sm.current = "main"
        
        else:
            invalid_aircraft()
        
        def create_aircraft_button(self):
            self.reset()
            sm.current = "Create"
        
        def reset(self):
            self.name.text = ""
            self.alt.text = ""
            self.speed.text = ""
            self.pos.text = ""
            self.direction.text = ""

class Main_Window(Screen):

    total_aircrafts = ObjectProperty(None)
    avg_alt = ObjectProperty(None)
    avg_speed = ObjectProperty(None)
    common_dir = ObjectProperty(None)
    









class MyApp(App):

    def build(self):
        pass

if __name__ == "__main__":
    MyApp().run()