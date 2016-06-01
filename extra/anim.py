from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.animation import Animation

class AnimWidget(Widget):
    pass
class AnimApp(App):
    def build(self):
        return AnimWidget()

    def crear_animacion(self):
        area_visualizacion = self.root.ids.area_visualizacion
        objeto = Factory.Cuadradito()
        objeto.x = self.root.width /2
        objeto.y = self.root.width /2
        area_visualizacion.add_widget(objeto)
        anim = Animation(x=objeto.x + 100, y=objeto.y+100, duration=.5)
        anim.start(objeto)


if __name__ == '__main__':
    AnimApp().run()
