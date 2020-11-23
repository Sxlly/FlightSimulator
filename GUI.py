import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Number Of Aircraft: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Aircraft Name: "))
        self.aircraftOne = TextInput(multiline = False)
        self.add_widget(self.aircraftOne)

        self.add_widget(Label(text="Aircraft Name 2: "))
        self.aircraftTwo = TextInput(multiline = False)
        self.add_widget(self.aircraftTwo)

        self.submit = Button(text = "Submit", font_size = 20)
        self.add_widget(self.submit)


class MyApp(App):

    def build(self):

        return MyGrid()

if __name__ == "__main__":
    MyApp().run()