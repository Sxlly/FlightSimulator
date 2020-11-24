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
        if (self.n_aircrafts != 0):
            Simulation.aircraft_count = int(self.n_aircrafts.text) 

            self.reset()

            sm.current = "enter"
        
        else:
            invalid_aircraft()
    
    def enter(self):
        self.reset()
        sm.current = "enter"
    
    def reset(self):
        self.n_aircrafts.text = ""

class Login_Window(Screen):

    n_aircrafts = ObjectProperty(None)

    def login_button(self):

        if Simulation.add_aircraft(self.n_aircrafts.text):
            MainWindow.current = self.n_aircrafts.text





class MyApp(App):

    def build(self):
        pass

if __name__ == "__main__":
    MyApp().run()