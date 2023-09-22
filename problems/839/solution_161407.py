import math
def carros (numerop):
    ''' dividir o número de pessoas por 5 que é a capacidade de cada carro, mas precisamos de uma
divisão exata porque não tem como levar 1 pessoa e meia '''
    nc=math.ceil(numerop/(5.0))
    return nc