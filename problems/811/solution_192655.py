def colchao(medidas,H,L):
    return ladom(H,L)
def ladom(H,L):
    if H >= L:
        return H + L
    else:
        retirn L + H