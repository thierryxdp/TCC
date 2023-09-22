def bombons(dinheiro, preco):
    return int(dinheiro / preco), dinheiro % preco
def falta(dinheiro, preco):
    n, troco = bombons(dinheiro, preco)
    return preco - troco