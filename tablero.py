import celdaVacia as cv
class tablero:
    _billetera = 100
    _costoCalle = 10
    _costoVecA = 20
    _costoVecB = 25
    _costoVecC = 30
    _costoDem = 5
    _celdas = [[None] * 5 for _ in range(5)]

    def __init__(self):
        for fila in range(5):
            for columna in range(5):
                celda_obj = cv.celdaVacia(columna, fila, self)  # Pasar el objeto tablero como tercer argumento
                self._celdas[columna][fila] = celda_obj

    def getBilletera(self):
        return "tienes " + str(self._billetera) + " pesos"
    
    def getCeldas(self):
        return self._celdas
    
    def getCelda(self,x,y):
        return self.getCeldas.__get__[x][y]
    
    def corroborarPos(self,x,y):
        return self.getCelda(x,y).tipo != "Vacia"