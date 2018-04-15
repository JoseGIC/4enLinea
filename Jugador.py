import Ficha


class Jugador:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.numFichas = 21
        self.puntos = 0
        self.ficha = Ficha.Ficha(color)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNumFichas(self):
        return self.numFichas

    def setNumFichas(self, numFichas):
        self.numFichas = numFichas

    def getPuntos(self):
        return self.puntos

    def setPuntos(self, puntos):
        self.puntos = puntos

    def getFicha(self):
        return self.ficha

    def setFicha(self, ficha):
        self.ficha = ficha