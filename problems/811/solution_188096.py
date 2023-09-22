def colchao(medidas,H,L):
    """verifica se o colchão novo passa pelas portas da casa de João"""
    """list, int, int -> bool"""
    medidas.remove(max(medidas))
    porta=[H,L]
    if (min(medidas)>min(porta) or max(medidas)>max(porta)):
    	return False
    else:
        return True