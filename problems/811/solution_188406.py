def colchao(medidas,H,L):
    ''''''
    medicas = [a,b,c]
    if H>c and a<H:
        return True
    if H>b and c<L:
        return True
    else:
        return False