def num_bombons(d,v):
    """Recebe os valores do total de dinheiro (d), o valor do bombom (v) e retorna quantidade comprável(q)"""
    import math
    q = d/v
    q = math.ceil(q)
    return q