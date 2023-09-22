def colchao(medidas,H,L):
    
    colchao=medidas[0]*medidas[2]
    porta= H*L
    
    if medidas[1]>H and medidas[2]>L:
        return 1==2
    if medidas[1]<=H and medidas[2]<L:
        return 1==1