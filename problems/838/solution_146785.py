import math

def num_bombons(dinheiro, valor):
    if dinheiro>=valor:
        return math.floor(dinheiro/valor)
    
    return "você não possui a quantidade mínima para comprar 1 bombom."