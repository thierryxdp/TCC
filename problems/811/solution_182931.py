def medidas(a,b,c):
    return (a,b,c)

def colchao (medidas, H, L):
    if medidas[0]*medidas[1]<H*L and medidas[0]*medidas[2]<H*L:
        return True
    
    if (b,c)>(H,L):
        return False