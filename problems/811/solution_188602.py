def colchao(medidas,H,L):
    if medidas[1:2]>[H] and medidas[1:2]>[L]:
        return False
    elif medidas[2:-1]>[H] and medidas[2:-1]>[L]:
        return False
    else:
        return True