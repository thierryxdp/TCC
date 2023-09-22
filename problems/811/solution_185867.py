def colchao(medidas : list,H : int,L : int)->bool:
    """ Dado as medidas A,B e C de um colchão, a altura H e 
    a largura L de uma porta, retorna se o colchão passa ou
    não passa por essa porta."""
    
    medidas = [A,B,C]
    
    if (A > H and A > L):
        if (B > L or B > H or C > L or C > H):
            return False
        else:
            return True
    if (B > H and B > L):
        if (A > L or A > H or C > L or C > H):
            return False
        else:
            return True
    if (C > H and C > L):
        if (A > L or A > H or B > L or B > H):
            return False
        else return True
    else:
        return True