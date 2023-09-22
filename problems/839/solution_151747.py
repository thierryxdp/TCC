from math import *
def carros(pessoas,lugares=5):
    '''Função que calcula a, quantidade de carros 
    necessários para acomodar um número de PESSOAS,
    considrando a quantidade de LUGARES do carro. 
    Se não for fornecida a quantidade de lugares do 
    carro, considera-se a capacidade convencional de 
    5 lugares.
    int,int->int''''
return ceil(pessoas/lugares)