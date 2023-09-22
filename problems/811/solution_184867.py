def colchao (lista,H,L):
    '''Dada as dimensoes do colchão a função retornará True se passar pela porta e 
    false se não passar. list,int,int->bool'''
    A= lista[0]
    B= lista[1]
    
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False