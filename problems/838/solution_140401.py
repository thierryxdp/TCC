import math

def num_bombons(preco:float, dinheiro:float) -> int:
    """Calcula quantos bombons são possíveis de comprar ao informar 
    o preço de cada e o total de dinheiro disponível"""

    return math.floor(dinheiro/preco)