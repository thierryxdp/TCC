#JUAN MERCES LEONEL
import math
def carros (passageiros, assentos=5):
    '''Vai dizer a quantidade de veículos para trnasportar os passageiros
    (se não for inserido a quantidade de assentos o código utilizará 5)'''
    return  math. ceil(passageiros/assentos)