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

"""Importing The Backend Classes"""
from Simulation import Simulation
from main import Aircraft


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        
        """Call grid layout constructor"""
        super(MyGridLayout, self).__init__(**kwargs)

        """Column Setting Within Grid"""
        self.cols = 1
        """Input Box Setting Within Grid"""
        self.add_widget(Label(text= "Number Of Aircraft: "))
        self.num_aircrafts = TextInput(multiline=False)
        self.add_widget(self.num_aircrafts)

        self.add_widget(Label(text= "Filename: "))
        self.filename = TextInput(multiline=False)
        self.add_widget(self.filename)

        """Button Setting Within Grid"""
        self.enter = Button(text = "Enter", font_size=32)
        #binding button to on press command
        self.enter.bind(on_press=self.press)
        self.add_widget(self.enter)

    def press(self, instance):
        num_aircrafts = self.num_aircrafts.text
        filename = self.filename.text

        #printing to terminal
        print(f'Current Number Of Aircraft In Airspace {num_aircrafts} and the Terrain File Is: {filename}')

        #printing to kivy current screen
        self.add_widget(Label(text= f'Current Number Of Aircraft In Airspace {num_aircrafts} and the Terrain File Is: {filename}'))

        #clear input boxs 
        self.num_aircrafts = ""
        self.filename = ""

"""App Run Class"""
class MyApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()