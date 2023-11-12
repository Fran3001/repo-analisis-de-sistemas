import celdaVacia as cv
import celdaCalle as cc
import celdaVecindarioA as cva
import celdaVecindarioB as cvb
import celdaVecindarioC as cvc
import celda as c

class tablero:
  _billetera = 100
  _costoDem = 5
  _celdas = [[None] * 5 for _ in range(5)]

  def __init__(self):
    self.vaciarTablero()

  def verTablero(self):
    celdas = self.getCeldas()
    for fila in celdas:
      for celda in fila:
        try:
          print(celda.getTipo(), end="\t")
        except AttributeError:
          print("None", end="\t")
      print()

  def vaciarTablero(self):
    for y in range(5):
      for x in range(5):
        celda_obj = cv.celdaVacia(x, y, self)
        self.setCelda(x, y, celda_obj)

  def getBilletera(self):
    return int(self._billetera)

  def setBilletera(self, cant):
    self._billetera += cant

  def _getCostoDem(self):
    return self._costoDem

  def getCeldas(self):
    return self._celdas

  def setCelda(self, y, x, celda):
    self._celdas[x][y] = celda

  def getCelda(self, x, y):
    return self.getCeldas()[y][x]

  def corroborarCeldaVacia(self, x, y):
    try:
      return self.getCelda(x, y).tipo is None
    except AttributeError:
      return True

  def corroborarPresupuesto(self, costo):
    try:
      return costo < self.getBilletera()
    except AttributeError:
      return False

  def corroborarTipo(self, tipo):
    if (tipo == "a"):
      celda__ = cva.celdaVecindarioA(0, 0, self)
      return celda__
    elif (tipo == "b"):
      celda__ = cvb.celdaVecindarioB(0, 0, self)
      return celda__
    else:
      celda__ = cvc.celdaVecindarioC(0, 0, self)
      return celda__

  def destruirCasilla(self):
    try:
      x = int(input("posicion de x de la casilla"))
      y = int(input("posicion de y de la casilla"))
      if (not (self.corroborarCeldaVacia(x, y))
          and self.corroborarPresupuesto(self._costoDem)):
        celdaNueva = cv.celdaVacia(x, y, self)
        self.setCelda(x, y, celdaNueva)
        self.setBilletera(-(celdaNueva.getPrecio()))
        print("Eliminado con exito!")
      else:
        print("error, no hay nada en esa casilla")
    except ValueError:
      print("Error: Ingrese valores válidos.")
    except Exception as e:
      print(f"Error: {e}")

  def cambiarTablero(self, x, y, celdaNueva):
    try:
      if (self.corroborarPresupuesto(celdaNueva.getPrecio())
          and self.corroborarCeldaVacia(x, y)):
        self.setCelda(x, y, celdaNueva)
        self.setBilletera(-(celdaNueva.getPrecio()))
        print("Agregado con exito!")
      else:
        print("error")
    except ValueError:
      print("Error: Ingrese valores válidos.")
    except Exception as e:
      print(f"Error: {e}")

  def construirCalle(self):
    try:
      x = int(input("posicion de x de la calle"))
      y = int(input("posicion de y de la calle"))
      celda_ = cc.celdaCalle(x, y, self)
      self.cambiarTablero(x, y, celda_)
    except ValueError:
      print("Error: Ingrese valores válidos.")
    except Exception as e:
      print(f"Error: {e}")

  def agregarVecindario(self, tipo):
    try:
      x = int(input("en que posicion x queres que vaya el vecindario?"))
      y = int(input("en que posicion y queres que vaya el vecindario?"))
      celda_ = self.corroborarTipo(tipo)
      if (celda_.corroborarVecinos(x, y, self)):
        self.cambiarTablero(x, y, celda_)
      else:
        print("error")
    except ValueError:
      print("Error: Ingrese valores válidos.")
    except Exception as e:
      print(f"Error: {e}")
