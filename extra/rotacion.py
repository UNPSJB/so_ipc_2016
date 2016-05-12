from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.properties import NumericProperty
from kivy.factory import Factory
from kivy.lang import Builder

class Ventana(Widget):
    pass


class RotacionApp(App):
    def build(self):
        return Ventana()

if __name__ == '__main__':
    RotacionApp().run()
