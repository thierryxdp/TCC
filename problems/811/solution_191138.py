def colchao(colchao, H, L):
    '''função que calcula se o colchão passa pelas dimensões da porta'''
    A = colchao[0]
    B = colchao[1]
    C = colchao[2]
    if A <= H and (B <= L or C <= L):
        return True
    if B <= H and (A <= L or C <= L):
        return True
    if C <= H and (A <= L or B <= L):
        return True
    else:
        return False