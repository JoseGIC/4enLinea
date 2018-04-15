import Jugador
import Tablero


class Partida:

    def cambiarTurno(turno):
        if turno == 1:
            return 2
        else:
            return 1

    nombre1 = raw_input("Nombre del jugador 1: ")
    nombre2 = raw_input("Nombre del jugador 2: ")

    jugador1 = Jugador.Jugador(nombre1, "rojo")
    jugador2 = Jugador.Jugador(nombre2, "amarillo")

    tablero = Tablero.Tablero()
    tablero.pintarse()

    turno = 1
    while jugador1.getNumFichas() > 0 or jugador2.getNumFichas() > 0:

        if turno == 1:
            jugadorActual = jugador1
        else:
            jugadorActual = jugador2

        print
        print "Turno del jugador %i (%s)" % (turno, jugadorActual.getNombre())
        print "Color de ficha %s (%c)" % (jugadorActual.getFicha().getColor(), jugadorActual.getFicha().pintarse())

        numColumna = input("Columna para colocar ficha: ")
        print
        if 0 < numColumna <= tablero.getNumColumnas():
            if tablero.ponerFicha(numColumna, jugadorActual.getFicha().getNumero()):
                print
                print "VICTORIA DEL JUGADOR %i (%s)!!" % (turno, jugadorActual.getNombre())
                break
            jugadorActual.setNumFichas(jugadorActual.getNumFichas() - 1)
            turno = cambiarTurno(turno)

        else:
            print
            print "ERROR: Introducir numeros del 1 al %i!!" % tablero.getNumColumnas()


    if jugador1.getNumFichas() == jugador2.getNumFichas() == 0:
        print
        print "EMPATE!!"