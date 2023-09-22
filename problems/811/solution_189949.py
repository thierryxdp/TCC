def colchao(medidas,H,L):
    
    medidas=[A,B,C]
    
    if ((medidas[0]<=H or L) and (medidas[1]<H or L)) or ((medidas[1]<=H or L) and (medidas[2]<=H or L)) or ((medidas[2]<=H or L) and (medidas[0]<=H or L)):
        return True
    else:
        return False