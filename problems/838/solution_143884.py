num_bombons(dinheiro,preco):
    """Função que calcula quantos bombons se podem comprar, dado uma quantia em dinheiro"""
    """float -> float"""
    bombons = dinheiro/preco
    return round(bombons)