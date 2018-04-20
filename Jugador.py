import Ficha


class Jugador:

    def __init__(self, nombre, numFichas, color):
        self.nombre = nombre
        self.numFichas = numFichas
        self.puntos = 210
        self.ficha = Ficha.Ficha(color)
        self.listaFichas = []

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

    def crearFichas(self):
        for i in range(0, self.numFichas):
            self.listaFichas.append(Ficha.Ficha(self.ficha.getColor()))

    def sacarFicha(self):
        if len(self.listaFichas) > 0:
            self.puntos -= 10
            return self.listaFichas.pop()
