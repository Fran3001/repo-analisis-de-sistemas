import tablero as t
import celda as c

mi_tablero = t.tablero()
rta = ""

while rta != "0":
  rta = input(
      "0 para terminar, 1 para ver tablero, 2 para ver tu plata, 3 para agregar un vecindario, 4 para destruir una casilla, 5 para agregar una calle \n"
  )
  if rta == "1":
    mi_tablero.verTablero()
  elif rta == "2":
    print(mi_tablero.getBilletera())
  elif rta == "3":
    rta2 = input("a(20 pesos), b(25 pesos) o c(30 pesos)? \n")
    if(rta2 == "a" or rta2 == "b" or rta2 == "c"):
      mi_tablero.agregarVecindario(rta2)
    else:
      print("El parametro es incorrecto")
  elif rta == "4":
    rta2= input("estas seguro que queres destruir una casilla? \n")
    if(rta2 == "si"):
      mi_tablero.destruirCasilla()
  elif rta == "5":
    rta2= input("estas seguro que queres contruir una casilla? \n")
    if(rta2 == "si"):
      mi_tablero.contruirCalle()

#qepd 
    