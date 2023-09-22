def colchao(medidas,H,L):
    porta=[H,L]
    medidas.sort(reverse=True)
    porta.sort(reverse=True)
    if medidas[0]<porta[0]:
        return True
    else:
        return False