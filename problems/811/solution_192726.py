def colchao(medidas,H,L):
    """Determina se joão consegue ou não passar o colchão pela porta"""
    if medidas[1]>= H:
        return True
    else:
        return False