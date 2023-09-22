from math import ceil
def carros(pessoas,lugares=5):
    '''retorna quantos carros serão necessários para a viagem dado o número de pessoas e o número de lugares dos carros, caso nenhum número de lugares seja dado será considerado = 5; int,int -> int'''
    return ceil(pessoas/lugares)