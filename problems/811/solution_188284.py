def teste(medidas,H,L):
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if b <= H:
        return True
    elif b > H:
        return False