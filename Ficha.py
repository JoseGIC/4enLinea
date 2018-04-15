class Ficha:

    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getNumero(self):
        if self.color == "rojo":
            return 1
        elif self.color == "amarillo":
            return 2

    def pintarse(self):
        if self.color == "rojo":
            return "x"
        elif self.color == "amarillo":
            return "o"