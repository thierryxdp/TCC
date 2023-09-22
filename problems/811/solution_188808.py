def colchao(medidas,H,L):
    """Função que retorna true ou false, dependendo se for 
    possível passar o colchão pela porta ou não
    list,int,int=>bool"""
    a = False
    b= False
    c = False
        
    if ((medidas[0]<=H or medidas[0] <= L) and (medidas[1]<=H or medidas[1]<=L)) or  ((medidas[0] <=H or medidas[0] <=L) and (medidas[2]<=H or medidas[2]<=L)):
        return True
    else:
        return False