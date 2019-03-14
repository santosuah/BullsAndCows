class NumeroRepetidoError(Exception):

    def __init__(self, valor):
        self.valor = valor

class LongitudClaveError(Exception):

    def __init__(self, longitud):
        self.longitud = longitud