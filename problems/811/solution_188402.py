def colchao(a,b,c,H,L):
    ''''''
    if H>c and a<H:
        return True
    if H>b and c<L:
        return True
    else:
        return False