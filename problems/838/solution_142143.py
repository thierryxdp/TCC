from math import floor
def num_bombons(saldo,valor_unitario):
    """calcula e retorna o numero maximo de bombons que Pedrinho consegue comprar, dados os valores de entrada do saldo e do preço unitario do bombom;
    float,float->int"""
    return floor(saldo/valor_unitario)