from config import longitudClave
from random import randint

class Creador(object):

    def __init__(self):
        self.__claveSecreta = self.__generarClave()

    def __generarClave(self):
        # Genera una clave en forma de lista de longitudClave
        # con valores entre 0 - 9 sin repeticiones

        clave = []
        while len(clave) < longitudClave:
            n = randint(0,9)
            if n not in clave:
                clave += [n]

        return clave
    
    def generarComprobacionFinal(self):
        return [longitudClave, 0]

    def imprimirClaveSecreta(self):
        print("  Secret key:", "".join([str(n) for n in self.__claveSecreta]))

    def puntuar(self, claveCandidata):
        
        aciertos = 0
        coincidencias = 0

        for i in range(longitudClave):
            if claveCandidata[i] == self.__claveSecreta[i]:
                aciertos += 1
            elif claveCandidata[i] in self.__claveSecreta:
                coincidencias += 1

        return [aciertos, coincidencias]
