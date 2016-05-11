from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.properties import NumericProperty
from kivy.factory import Factory

from math import pi, sin, cos

CIRCUNFERENCIA = 2*pi
GRADO = CIRCUNFERENCIA / 360.0


class Ventana(Widget):
    pass


class Dibujo(Widget):
    # Propiedades, para ser binculadas en el .kv
    elementos = NumericProperty(1)
    radio = NumericProperty(50)

    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        print kwargs
        # Cuando cambie alguna propiedad, llamar a redibujar
        self.bind(elementos=self.redibujar)
        self.bind(radio=self.redibujar)

    def redibujar(self, obj, valor):
        self.canvas.clear()
        with self.canvas:
            #Color(1, 0, 0, 1)
            salto_angular = CIRCUNFERENCIA / self.elementos
            for i in range(self.elementos):
                angulo = i * salto_angular
                x = cos(angulo) * self.radio + self.width / 2
                y = sin(angulo) * self.radio + self.height / 2
                #Ellipse(pos=(x, y), size=(10, 10))
                if i % 2 == 0:
                    imagen = 'emoji.png'
                else:
                    imagen='minion.png'
                Rectangle(
                    pos=(x, y),
                    source=imagen,
                    #size=(10, 10)
                )



class TrigonometriaApp(App):
    def build(self):
        return Ventana()

if __name__ == '__main__':
    TrigonometriaApp().run()
