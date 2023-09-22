def colchao(medidas,H,L):
    a=0
    b=0
    c=0
    if medidas[0]<=H or medidas[0]<=L:
        a=1
    elif medidas[1]<=H or medidas[1]<=L:
        b=1
    elif medidas[2]<=H or medidas[2]<=L:
        c=1
        
        
	d = a+b+c
    if d>=2:
        return True
    else:
        return False