def colchao(medidas : list,H : int,L : int)->bool:
    """ Dado as medidas A,B e C de um colchão, a altura H e 
    a largura L de uma porta, retorna se o colchão passa ou
    não passa por essa porta."""
    
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if (A > H and A > L):
        if ((B > L and B > H) or (C > L and C > H)):
            return False
        if ((B > L and C > L) or (B > H and C > H)):
            return False
        else:
            return True
        
    if (B > H and B > L):
        if ((A > L and A > H) or (C > L and C > H)):
            return False
        if ((A > L and C > L) or (A > H and C > H)):
            return False
        else:
            return True
        
    if (C > H and C > L):
        if ((A > L and A > H) or (B > L and B > H)):
            return False
        if ((A > L and B > L) or (A > H and B > H)):
            return False
        else:
            return True
    
    else:
        return True