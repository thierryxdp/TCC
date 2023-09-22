def colchao(medidas,H,L):
    """verifica se o colchão novo passa pelas portas da casa de João"""
    """list, int, int -> bool"""
    medidas_menor=medidas-list(max(medidas))
    return not(max(medidas_menor)>max(H,L) or min(medidas_menor)>min(H,L))