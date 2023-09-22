def colchao(medidas,H,L):
    
    colchao=medidas[1]*medidas[2]
    porta= H*L
    
    if medidas[1]>H:
        return 1==2
    if colchao< porta:
        return 1==1