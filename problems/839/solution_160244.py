from math import*
def carros(pessoas, capacidade=5):
    '''(int, int=>int)'''
    automoveis = .ceil(pessoas/capacidade)
    return automoveis