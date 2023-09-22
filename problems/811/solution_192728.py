def colchao(medidas,H,L):
    """Determina se joão consegue ou não passar o colchão pela porta"""
    if medidas[1]<= H or medidas[2]<=L:
        return True
    else:
        return False