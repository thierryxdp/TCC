import math
def num_bombons(dinheiro,preco):
    """Função que retorna a quantos bombons é possível comprar dados o preço do bombom e o dinheiro."""
    if dinheiro<preco:
        return 0
    else:
        return math.floor(dinheiro/preco)