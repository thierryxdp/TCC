def colchao(medidas, H, L):
    
    
    """ Dadas as medidas do colchão e da porta retorna True se o Colchão passar pela porta e False se não passar
     int, int, int -> bool   """
    
    if medidas [1]<H or medidas [2]<L:
        
        return True
    else:
        
        return False