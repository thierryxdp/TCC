def num_bombons(dinheiro,preco):
    """Função que calcula quantos bombons se podem comprar, dado uma quantia em dinheiro"""
    """float,float -> int"""
    bombons = dinheiro/preco
    return math.floor(bombons)