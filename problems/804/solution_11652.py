def filtra_pares(t):
    '''
    	Função recebe uma tupla(t) com quatro elementos
        inteiros e retorna outra tupla só com os elementos 
        pares de t na mesma ordem que eles estavem
        tuple -> tuple
        
    '''
    
    pares = (p1,p2,p3,p4)
    
    if ((t[0])%(2))==0:
        pares = pares[::4]
    if ((t[1])%(2))==0:
        pares = pares[-1::3]
    if ((t[2])%(2))==0:
        pares = pares[-2::2]
    if ((t[3])%(2))==0:
        pares = pares[1::4]
    return pares