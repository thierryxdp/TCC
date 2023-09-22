def colchao(medidas,H,L):
    """verifica se o colchão novo passa pelas portas da casa de João"""
    """list, int, int -> bool"""
    medidas_menor=medidas.remove(max(medidas))
    porta=[H,L]
    if (min(medidas_menor)>min(porta) or max(medidas_menor)>max(porta):
    	return False
    else:
        return True