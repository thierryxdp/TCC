def colchao(medidas,H,L):
    for x in medidas:
        if x > H or x > L:
            return False
        elif x>H and x > L:
            return False
        else:
            return True