#!/usr/bin/env python

from kivy.support import install_twisted_reactor
install_twisted_reactor()

import sys
import subprocess
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.factory import Factory
from leer_struct import buscar_estructura
from threading import Thread

TMensaje = buscar_estructura(
    './c/comm.h',
    'TMensaje'
)
from twisted.internet import protocol, reactor

class EscuchaC(protocol.Protocol):
    def __init__(self, app):
        self.app = app
    def datagramReceived(self, data, direccion):
        m = TMensaje()
        m.unpack(data)
        self.app.llego_mensaje(m)

print TMensaje
class Ventana(Widget):
    pass


class PongApp(App):

    procesos = {}

    def build(self):
        reactor.listenUDP(2016, EscuchaC(self))
        return Ventana()

    def morir(self):
        sys.exit(1)
    def compilar(self):
        subprocess.call(
            'gcc ./c/comm.c ./c/prog_a.c -o ./c/prog_a &&'
            'gcc ./c/comm.c ./c/prog_b.c -o ./c/prog_b &&'
            'echo "Compilacion OK"', shell=True)
    def ejecutar(self, comando):
        hilo = Thread(target=subprocess.call,
        args=(comando,))
        hilo.start()
        #subprocess.call(comando)
    def agregar_coso(self):
        #import pdb; pdb.set_trace()
        coso = Factory.Coso()
        self.root.ids.vis.add_widget(coso,
        )
    def llego_mensaje(self, mensaje):

        if not mensaje.pid in self.procesos:
            grafico = Factory.Proceso(
                x=mensaje.x,
                y=mensaje.y
            )
            self.root.ids.vis.add_widget(grafico)
            self.procesos[mensaje.pid] = grafico

if __name__ == '__main__':
    PongApp().run()
