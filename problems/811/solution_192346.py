def colchao(medidas,H,L):
    if medidas[0:1]<H or medidas[0:1]<L:
        return True
    if medidas[2:5]<H or medidas[2:5]<L:
        return True
    if medidas[6:9]<H or medidas[6:9]<L:
        return True
    else:
        return False