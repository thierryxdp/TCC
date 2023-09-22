def colchao(medidas,H,L):
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if (b<=h and a<=L) or (b<=L and a<=H):
        return True
    else:
        return False