def colchao(medidas,H,L):
    '''Retorna se o colchão passa ou não pela porta da casa, dadas as medidas do colchão e H e L da porta'''
    '''list[int,int,int],int,int,int -> bool'''
    if((medidas[0]<=H or medidas[0]<=L) and (medidas[1]<=H or medidas[1]<=L)) or ((medidas[0]<=H or medidas[0]<=L) and (medidas[2]<=H or medidas[2]<=L))or ((medidas[2]<=H or medidas[2]<=L) and (medidas[1]<=H or medidas[1]<=L)):
        return True
    else:
        return False