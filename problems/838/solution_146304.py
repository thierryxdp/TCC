def num_bombons(dinheiro,preco):
    return float(dinheiro/preco) and dinheiro%preco
def falta(dinheiro,preco):
    n,troco = bombons(dinheiro,preco)
    return preco-troco