class Ficha:

    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def pintarse(self):
        if self.color == "rojo":
            return "x"
        else:
            return "o"
