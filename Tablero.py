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

    def getDiagonalCreciente(self, numFila, numColumna):
        diagonal = []
        filaActual = numFila - 1
        columnaActual = numColumna - 1

        while filaActual != self.numFilas - 1 and columnaActual != 0:
            filaActual += 1
            columnaActual -= 1

        while filaActual >= 0 and columnaActual < self.numColumnas:
            diagonal.append(self.matriz[filaActual][columnaActual])
            filaActual -= 1
            columnaActual += 1

        return diagonal

    def getDiagonalDecreciente(self, numFila, numColumna):
        diagonal = []
        filaActual = numFila - 1
        columnaActual = numColumna - 1

        while filaActual != 0 and columnaActual != 0:
            filaActual -= 1
            columnaActual -= 1

        while filaActual < self.numFilas and columnaActual < self.numColumnas:
            diagonal.append(self.matriz[filaActual][columnaActual])
            filaActual += 1
            columnaActual += 1

        return diagonal

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
                return self.comprobarLineas(i + 1, numColumna, ficha)
        return False

    def comprobarLineas(self, numFila, numColumna, ficha):
        fila = self.getFila(numFila)
        columna = self.getColumna(numColumna)
        diagonalDcha = self.getDiagonalCreciente(numFila, numColumna)
        diagonaIzda = self.getDiagonalDecreciente(numFila, numColumna)

        return self.lineaHecha(fila, ficha) or \
                self.lineaHecha(columna, ficha) or \
                self.lineaHecha(diagonalDcha, ficha) or \
                self.lineaHecha(diagonaIzda, ficha)

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