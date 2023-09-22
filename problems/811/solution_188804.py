def colchao(medidas,H,L):
    a = False
    b= False
    c = False
        
    if (medidas[1]<=H or medidas[1]<=L) or  (medidas[2]<=H or medidas[2]<=L):
        return True
    else:
        return False