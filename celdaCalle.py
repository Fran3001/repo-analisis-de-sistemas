import celda as c

class celdaCalle(c.celda):
  def __init__(self, tablero, x_pos, y_pos):
      super().__init__(tablero, x_pos, y_pos)
      self.tipo = "Calle"
      self.precio = 10

