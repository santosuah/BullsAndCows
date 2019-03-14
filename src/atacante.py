from error import LongitudClaveError, NumeroRepetidoError
from config import longitudClave
from random import choice
from sys import exit

class Atacante(object):

    def __init__(self):
        self.__claveActual = []

    def deducirClave(self):

        pedida = False
        while not pedida:

            try:
                self.__claveActual = [int(i) for i in input("  Input: ").split(",")]

                if (len(self.__claveActual) != longitudClave):
                    raise LongitudClaveError(len(self.__claveActual))
                
                elif len(set(self.__claveActual)) != longitudClave:
                    raise NumeroRepetidoError(self.__claveActual)
                
                else:
                    pedida = True

            except ValueError:
                print("  Error: Invalid input, format {w,x,y,z} \n")

            except LongitudClaveError as lce:
                print("  Error: Key length (" + str(lce.longitud) + ") must be (" + str(longitudClave) + ")\n")

            except NumeroRepetidoError:
                print("  Error: Repeated numbers in key\n")

            except (KeyboardInterrupt, SystemExit):
                print("KeyboardInterrupt\n")
                exit(0)

        return self.__claveActual
