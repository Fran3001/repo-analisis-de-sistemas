import celda as c

class celdaVacia(c.celda):
    def __init__(self, x_pos, y_pos, tablero):
        super().__init__(x_pos, y_pos, tablero)
        self.tipo = "Vacia"