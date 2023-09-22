#float float -> int float
def bombons(dinheiro, preco):
    return int(1.0/0.5), dinheiro % preco
    
# Calcula quanto falta para mais um bombom
# float float -> float
def falta(dinheiro, preco):
    n, troco = bombons(dinheiro, preco)
    return preco - troco sua função aqui. Pode apagar essa linha.