from math import ceil

def carros (p,c=5):
    '''
    Calcule a quantidade de veículos necessários

    Uso:
    carros (p,c=5)

    Entrada:
    - p (float, obrigatório): quantidade de pessoas
    - c (float, opcional, padrão 5): capacidade do carro
    Se não fornecido, calcula a quantidade usando 5.

    Saída:
    - quantidade de veículos necessários (float)
    '''
    return ceil (p/c)