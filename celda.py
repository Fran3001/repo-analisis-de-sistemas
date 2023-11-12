class celda:

  def __init__(self, x_pos, y_pos, tablero):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.tablero = tablero
    self.precio = 0
    self.tipo = None

  def getPosX(self):
    return self.x_pos

  def getPosY(self):
    return self.y_pos

  def getPrecio(self):
    return self.precio

  def getTablero(self):
    return self.tablero

  def getTipo(self):
    return self.tipo

  def corroborarVecinos(self, x, y, tablero):
    vec1 = self.getTablero().getCelda(x + 1, y) if x + 1 < 5 else None
    vec2 = self.getTablero().getCelda(x - 1, y) if x - 1 >= 0 else None
    vec3 = self.getTablero().getCelda(x, y + 1) if y + 1 < 5 else None
    vec4 = self.getTablero().getCelda(x, y - 1) if y - 1 >= 0 else None

    if (vec1 and vec1.getTipo() == "Calle") or (vec2 and vec2.getTipo() == "Calle") or (vec3 and vec3.getTipo() ==           "Calle") or (vec4 and vec4.getTipo() == "Calle"):
      return True
    else:
      print(
          "no hay ninguna calle alrededor por lo que no se puede poner el vecindario"
      )
      return None
