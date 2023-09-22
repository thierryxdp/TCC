#Calcula quantos bombons e troco
# float float -> int float
def bombons(dinheiro, preco):
    return int(dinheiro / preco), dinheiro % preco