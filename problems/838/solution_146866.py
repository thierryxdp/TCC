import math

def num_bombons(dinheiro, valor):
    #verifica se a pessoa tem o mínimo necessário
    if dinheiro>=valor:
        #arredonda para baixo a quantidade de bombons
        return math.floor(dinheiro/valor)    
    return 0