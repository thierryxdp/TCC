def colchao(medidas,H,L):
    "retorna se o colchão passa ou não pela porta"
    medidas.sort()
    if medidas[0] > L:
        if medidas[0] > H:
            return False
        elif medidas[1] > L:
            return False
        else:
            return True
    elif medidas[1] > H:
        return False
    else:
        return True