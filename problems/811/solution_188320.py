def colchao(medidas,H,L):
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if (((b <= H) and (a>L)) or ((b<= H) and (a<L))):
        return True
    else:
        return False