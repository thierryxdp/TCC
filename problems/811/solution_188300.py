def colchao(medidas,H,L):
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if ((b <= H) and (c>L)) or ((b<= H) and (c<L)):
        return True
    elif (b > H) or (c<L):
        return False