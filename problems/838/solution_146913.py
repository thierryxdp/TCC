# Calcula quantos bombons e troco
# float float -> int float
def num_bombons(dinheiro, preco):
    return int(dinheiro / preco), dinheiro % preco
    
# Calcula quanto falta para mais um bombom
# float float -> float
def falta(dinheiro, preco):
    n, troco = num_bombons(dinheiro, preco)
    return preco - troco