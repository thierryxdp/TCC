def colchao(lista,M,L):
    """funcao que determina se o colchao passa pela porta ou nao"""
    """list,float,float->bool"""
    A = lista[0]
    B = lista[1]
    
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False