# Quantos bombons posso comprar
# número número -> int
def qtd_bombons_dec(dinheiro, preco):
    return int(dinheiro / preco)

# Qual o troco da compra
# número númer -> número
def troco_bombons_dec(dinheiro, preco):
    return dinheiro % preco

# Quantos bombons e qual o troco
# número número -> int número
def bombons_dec(dinheiro, preco):
    return qtd_bombons_dec(dinheiro, preco), troco_bombons_dec(dinheiro, preco)

# Quantos bombons posso comprar
# int int -> int
def qtd_bombons_int(dinheiro, preco):
    return dinheiro / preco

def troco_bombons_dec(dinheiro, preco):
    return dinheiro % preco

# Quantos bombons e qual o troco
# Valores em reais
# número número -> int número
def bombons_int(dinheiro, preco):
    dinheiro_cent = int(dinheiro * 100)
    preco_cent = int(preco * 100)
    return qtd_bombons_int(dinheiro, preco), troco_bombons_int(dinheiro, preco) / 100.0