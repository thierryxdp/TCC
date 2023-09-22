def uppCons(frase):
    """..."""
    x = 0
    y = list(frase)
    z = []
    while x < len(y):
        if y[x] in [B,C,D,F,G,H,JK,L,M,N,P,Q,R,S,T,V,W,X,Y,Z]:
            z = z + y[x]
        else:
            None
        x = x + 1
    return z