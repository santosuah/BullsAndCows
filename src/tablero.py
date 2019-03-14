from os import system
from creador import Creador
from atacante import Atacante
from config import esquina, horizontal, vertical, maxIteraciones

class Tablero(object):

    def __init__(self):
        self.__jugadorAtacante = Atacante()
        self.__jugadorCreador = Creador()
        self.__celdas = []


    def __imprimirNombre(self):
        print("\n  ====================")
        print("  == Bulls and Cows ==")
        print("  ====================\n")


    def __generarCadenaTabla(self, lista):

        superior = esquina
        media = horizontal

        for i in range(len(lista)):
            superior += vertical
            if lista[i] == -1: superior += "-"
            superior += esquina
            media += " " + str(lista[i]) + " " + horizontal

        return superior, media


    def __imprimirCeldas(self, iteracion, comprobacion, candidata):
        
        x2, y2 = self.__generarCadenaTabla(candidata)
        x3, y3 = self.__generarCadenaTabla(comprobacion)

        x = "     " + x2 + "  " + x3
        y = "  " + str(iteracion) + "  " + y2 + "  " + y3

        print(x, y, x, sep="\n")


    def __imprimirTablero(self):

        self.__imprimirNombre()
        print("  I        Guess        Bulls Cows")

        for fila in self.__celdas:

            x2, y2 = self.__generarCadenaTabla(fila[1])
            x3, y3 = self.__generarCadenaTabla(fila[2])

            x = "     " + x2 + "  " + x3

            if fila[0] > 9: valor = 1
            else: valor = 2
            
            y = "  " + str(fila[0]) + " "*valor + y2 + "  " + y3

            print(x, y, sep="\n")

        print(x)


    def jugar(self):

        system("cls||clear")

        # Imprime nombre del juego
        self.__imprimirNombre()

        # La lisa con el resultado que se obtiene al
        # adivinar la clave completa
        comprobacionFinal = self.__jugadorCreador.generarComprobacionFinal()

        # Bucle de iteraciones
        for i in range(1, maxIteraciones+1):
            
            # El atacante escoje una clave en base al estado
            # que previamente puede haber sido cribado
            candidata = self.__jugadorAtacante.deducirClave()
            system("cls||clear")

            # El jugador creador calcula las coincidencias entre la clave
            # candidata del atacante y la clave secreta.
            comprobacion = self.__jugadorCreador.puntuar(candidata)

            # Añadimos la jugada al tablero
            self.__celdas.append([i,candidata,comprobacion])

            # Imprime el table con las fichas actualizadas
            self.__imprimirTablero()

            # si la comprobacion es igual a la final
            # el atacante ha averiguado la clave
            # termina el juego
            if (comprobacion == comprobacionFinal):
                print("\n  You win!\n")
                return
            
            else:
                # Cribamos el estado con la comprobacion no final
                #self.__jugadorAtacante.cribarEstado(comprobacion)

                # self.__jugadorAtacante.imprimirEstado()
                print()
        
        print("  You lost!\n")
        self.__jugadorCreador.imprimirClaveSecreta()
        print()
        return
