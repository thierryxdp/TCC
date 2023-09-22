from math import ceil
def carros(numero_pessoas, capacidade = 5):
    '''Função que calcula o número de carros necessários
    para transportar um número de pessoas dado o total de
    integrantes e a capacidade dos veículos. Caso não seja
    informada a capacidade será usada o valor convencional
    das regras rodoviárias
    int, int -> int'''
    return ceil(numero_pessoas/capacidade)