def colchao(medidas,H,L):
    """retorne se o colchão passa pela porta da casa"""
    if medidas[1]<L or medidas[0]<H:
        return True
    else:
        return False