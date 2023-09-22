def colchao(medidas,H,L):
    return tuple(ladom(H,L))
def ladom(H,L):
    if H >= L:
        return str(H) + " " + str(L)
    else:
        return str(L) + " " + str(H)