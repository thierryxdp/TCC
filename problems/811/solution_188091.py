def colchao(medidas,H,L):
    """verifica se o colchão novo passa pelas portas da casa de João"""
    """list, int, int -> bool"""
    medidas_menor=medidas.remove(max(medidas))
    porta=[H,L]
    return not(max(medidas_menor)>max(porta) or min(medidas_menor)>min(porta))