def colchao(medidas,H,L):
    for x in medidas[1:]:
        if x > H or x > L:
            return False

        else:
            return True