import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    n_aircrafts = ObjectProperty(None)
    pass

    def n_aircrafts_button(self):
        print("Number Of Aircrafts: ", self.n_aircrafts.text)
        self.n_aircrafts.text = ""


class MyApp(App):

    def build(self):

        return MyGrid()
        return FloatLayout()

if __name__ == "__main__":
    MyApp().run()