import math
def carros(n,c=5):
    '''Funçao que calcula o numero de veiculos necessarios para transportar determinada quantidade de pessoas,
    caso o veiculo seja convencional, ou seja, possuem capacidade para 5 pessoas, apenas a quantidade de pessoas
    basta, caso contrario, na primeira entrada deve ser inserido o numero de pessoas e na segunda a capacidade do veiculo;
    int, int -> int'''
    return math.ceil(n/c)