from math import ceil

def carros(x,y=5):
    '''
    Calcula a quantidade de carros com y vagas para transportar x passsageiros em uma viagem. Se y não for definido, será tomado com 5 vagas.
    '''
    return ceil(x/y)