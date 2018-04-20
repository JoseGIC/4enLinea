import pickle
import Jugador
import Tablero


class Partida:

    print
    print " ------------"
    print "| 4 EN LINEA |"
    print " ------------"
    print

    while True:
        print "1. Nueva partida"
        print "2. Cargar partida"
        print "================="
        print

        modoDeJuego = input("Modo de juego: ")
        print

        if modoDeJuego == 1:
            nombre1 = raw_input("Nombre del jugador 1: ")
            nombre2 = raw_input("Nombre del jugador 2: ")

            jugador1 = Jugador.Jugador(nombre1, 21,"rojo")
            jugador2 = Jugador.Jugador(nombre2, 21, "amarillo")

            jugador1.crearFichas()
            jugador2.crearFichas()

            tablero = Tablero.Tablero()
            turno = 1

            break

        elif modoDeJuego == 2:
            with open('partidaGuardada.pkl', 'rb') as binario:
                jugador1 = pickle.load(binario)
                jugador2 = pickle.load(binario)
                tablero = pickle.load(binario)
                turno = pickle.load(binario)

                binario.close()
                print "Partida cargada!"
                print
            break

        else:
            print "ERROR: Elige un modo de juego valido!"

    print
    tablero.pintarse()

    while jugador1.getNumFichas() > 0 or jugador2.getNumFichas() > 0:

        if turno == 1:
            jugadorActual = jugador1
        else:
            jugadorActual = jugador2

        print
        print "Turno del jugador %i (%s)" % (turno, jugadorActual.getNombre())
        print "Color de ficha %s (%c)" % (jugadorActual.getFicha().getColor(), jugadorActual.getFicha().pintarse())

        numColumna = input("Numero de columna (0 para guardar partida): ")
        print

        if numColumna == 0:
            with open('partidaGuardada.pkl', 'wb') as binario:
                pickle.dump(jugador1, binario, pickle.HIGHEST_PROTOCOL)
                pickle.dump(jugador2, binario, pickle.HIGHEST_PROTOCOL)
                pickle.dump(tablero, binario, pickle.HIGHEST_PROTOCOL)
                pickle.dump(turno, binario, pickle.HIGHEST_PROTOCOL)

                binario.close()
                print
                print "Partida guardada!"
                print

            break

        elif 0 < numColumna <= tablero.getNumColumnas():
            if tablero.ponerFicha(numColumna, jugadorActual.sacarFicha().getNumero()):
                print
                print "VICTORIA DEL JUGADOR %i (%s: %i puntos)!!" % (turno, jugadorActual.getNombre(), jugadorActual.getPuntos())
                break

            jugadorActual.setNumFichas(jugadorActual.getNumFichas() - 1)
            if turno == 1:
                turno = 2
            else:
                turno = 1

        else:
            print
            print "ERROR: Introducir numeros del 1 al %i o 0 para guardar." % tablero.getNumColumnas()

    if jugador1.getNumFichas() == jugador2.getNumFichas() == 0:
        print
        print "EMPATE!!"
