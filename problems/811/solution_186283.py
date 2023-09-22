def colchao(medidas,H,L):
    
    colchao=medidas[0]*medidas[1]
    porta= H*L
    
    if medidas[1]>H:
        return 1==2
    if colchao< porta:
        return 1==1