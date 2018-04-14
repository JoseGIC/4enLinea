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

    def getFila(self, numFila):
        return self.matriz[numFila - 1]

    def getColumna(self, numColumna):
        columna = []
        for i in range(self.numFilas):
            columna.append(self.matriz[i][numColumna - 1])
        return columna


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

    def mostrarse(self):
        for i in range(self.numFilas):
            print self.matriz[i]


    def ponerFicha(self, numColumna, ficha):
        for i in reversed(range(self.numFilas)):
            if self.matriz[i][numColumna - 1] == 0:
                self.matriz[i][numColumna - 1] = ficha
                self.pintarse()
                self.comprobarLineas(i + 1, numColumna, ficha)
                break

    def comprobarLineas(self, numFila, numColumna, ficha):
        fila = self.getFila(numFila)
        columna = self.getColumna(numColumna)
        #diagonalDcha = ...
        #diagonaIzda = ...
        linea = self.lineaHecha(fila, ficha) or \
                self.lineaHecha(columna, ficha) #or \
                #self.lineaHecha(diagonalDcha, ficha) or \
                #self.lineaHecha(diagonaIzda, ficha)
        if linea:
            print "VICTORIA!"

    def lineaHecha(self, linea, ficha):
        total = 0
        for i in linea:
            if i == ficha:
                total += 1
                if total == 4:
                    return True
            else:
                total = 0
        return False

    def diagonalHecha(self, fila, columna, ficha):
        pass


t1 = Tablero()
t1.ponerFicha(4, 1)
t1.ponerFicha(2, 1)
t1.ponerFicha(2, 2)
t1.ponerFicha(3, 2)
t1.ponerFicha(2, 2)
t1.ponerFicha(5, 1)
t1.ponerFicha(6, 1)
#t1.ponerFicha(7, 1)
t1.ponerFicha(2, 2)
t1.ponerFicha(2, 2)