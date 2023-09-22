def colchao(medidas,H,L):
    a = False
    b= False
    c = False
        
    if not((medidas[0]<=H or medidas[0]<=L and medidas[1]<=H or medidas[1]<=L) or (medidas[0]<=H or medidas[0]<=L and medidas[2]<=H or medidas[2]<=L)):
        return False
    else:
        return True