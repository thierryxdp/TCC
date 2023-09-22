from math import ceil
def carros (pessoas, capacidade=5):
    '''funcao que calcula e retorna a quantidade de carros necessaria para uma viagem tendo
    o numero de pessoas e a capacidade do veiculo como entradas'''
    return ceil(pessoas/capacidade)