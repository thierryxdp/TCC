# Calcula quanto falta para mais um bombom
# float float -> float
def falta(dinheiro, preco):
    n, troco = num_bombons(dinheiro, preco)
    return preco - troco