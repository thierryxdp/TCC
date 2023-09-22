def colchao(medidas,H,L):
    medidas.sort(reverse=True)
    if medidas[1]<=H:
        return True
    else:
        return False