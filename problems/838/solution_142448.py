def num_bombons (d,p):
    """calcula quantos bombons podem ser comprados, em função do dinheiro d e do preço do bombom p"""
    return min(d/p)