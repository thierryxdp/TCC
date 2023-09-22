def tamanho_colchao(medidas,H,L):
    """verifica se o colchão novo passa pelas portas da casa de João"""
    """list, int, int -> bool"""
    medidas_menor=medidas-[max(medidas)]
    return max(medidas_menor)>(H or L)