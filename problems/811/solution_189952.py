def colchao(medidas,H,L):
    
    [A,B,C]=medidas
    
    if ((medidas[0]<=H) and (medidas[1]<=L)) or ((medidas[1]<=H) and (medidas[2]<=L)) or ((medidas[2]<=H) and (medidas[0]<=L)):
        return True
    else:
        return False