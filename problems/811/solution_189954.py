def colchao(medidas,H,L):
    
    [A,B,C]=medidas
    
    if ((medidas[0]<=H) and (medidas[1]<=L)) or ((medidas[1]<=H) and (medidas[2]<=L)) or ((medidas[2]<=H) and (medidas[0]<=L)) or ((medidas[0]<=L) and (medidas[1]<=H)) or ((medidas[1]<=L) and (medidas[2]<=H)) or ((medidas[2]<=L) and (medidas[0]<=H)):
        return True
    else:
        return False