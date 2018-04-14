class Tablero:

    def __init__(self):
        self.numFilas = 6
        self.numColumnas = 7
        self.vacio = True
        self.matriz = [[0] * self.numColumnas for i in range (self.numFilas)]
        self.casillaVacia = "."


    def getNumFilas(self):
        return self.numFilas

    def setNumFilas(self, numFilas):
        self.numFilas = numFilas

    def getNumColumnas(self):
        return self.numColumnas

    def setNumColumnas(self, numColumnas):
        self.numColumnas = numColumnas

    def getVacio(self):
        return self.vacio

    def setVacio(self, vacio):
        self.vacio = vacio

    def getMatriz(self):
        return self.matriz

    def setMatriz(self, matriz):
        self.matriz = matriz


    def pintarse(self):
        for i in range(self.numFilas):
            for j in range(self.numColumnas):
                if self.matriz[i][j] == 0:
                    print ".",
                elif self.matriz[i][j] == 1:
                    print "x",
                elif self.matriz[i][j] == 2:
                    print "o",
            print
        print

    def mostrarse (self):
        for i in range(self.numFilas):
            print self.matriz[i]

    def ponerFicha(self, columna, ficha):
        for i in reversed (range(self.numFilas)):
            if self.matriz[i][columna - 1] == 0:
                self.matriz[i][columna - 1] = ficha
                break

t1 = Tablero()
t1.pintarse()
t1.ponerFicha(4, 1)
t1.pintarse()
t1.ponerFicha(2, 1)
t1.pintarse()
t1.ponerFicha(2, 2)
t1.pintarse()
t1.ponerFicha(3, 2)
t1.pintarse()
t1.ponerFicha(2, 2)
t1.pintarse()
t1.mostrarse()
