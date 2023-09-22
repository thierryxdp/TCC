from math import ceil
def carros(qtd_pessoas, capacidade=5):
    ''' calcula quantos carros são necessários para transportar
    a quantidade de pessoas indicadas. Caso a capacidade dos carros
    não seja indicada, é considerada como sendo o padrão de 5.
    int, int(opcional) --> int'''
    return ceil(qtd_pessoas/capacidade)