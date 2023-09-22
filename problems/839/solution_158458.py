from math import ceil

def carros(pessoas,capacidade=5):
    '''funcao que define o numero de carros necessarios
    para que uma viagem ocorra de acordo com as regras
    da rodoviaria, sendo que cada carro convencional 
    tem a capacidade de 5 pessoas
    '''
    return ceil(pessoas/capacidade)