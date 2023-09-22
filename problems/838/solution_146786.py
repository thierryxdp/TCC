import math

def num_bombons(dinheiro, valor):
    if dinheiro>=valor:
        return math.floor(dinheiro/valor)
    
    return 0