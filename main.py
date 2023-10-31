import tablero as t
import celda as c

mi_tablero = t.tablero()
rta = ""

while rta != "0":
    rta = input("0 para terminar, 1 para ver tablero, 2 para ver tu plata, 3 para agregar una casaA")
    if rta == "1":
      celdas = mi_tablero.getCeldas()
      for fila in celdas:
        for celda_ in fila:
          print(celda_.getTipo(), end="\t")  
        print()  
    elif rta == "2":
      print(mi_tablero.getBilletera())
    elif rta == "3":
      x = input("en que posicion x queres que vaya la casa?")
      y = input("en que posicion y queres que vaya la casa?")
      print(mi_tablero.corroborarPos(x,y))

