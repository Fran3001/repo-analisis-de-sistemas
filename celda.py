import tablero as t

class celda:
    def __init__(self, x_pos, y_pos, tablero):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tablero = tablero
        self.tipo = ""

    def getPosX(self):
        return self.x_pos

    def getPosY(self):
        return self.y_pos
    
    def getTablero(self):
        return self.tablero
    
    def getTipo(self):
        return self.tipo
