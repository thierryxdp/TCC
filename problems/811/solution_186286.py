def colchao(medidas,H,L):
    
    colchao=medidas[1]*medidas[2]
    porta= H*L
    
    if colchao>porta:
        return 1==2
    if colchao<= porta:
        return 1==1