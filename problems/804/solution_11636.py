filtra_pares(t):
    '''
    	Função recebe uma tupla(t) com quatro elementos
        inteiros e retorna outra tupla só com os elementos 
        pares de t na mesma ordem que eles estavem
        tuple -> tuple
        
    '''
    
    pares = (p1,p2,p3,p4)
    
    if t[0]%2==0:
        pares = pares[0]
    if t[1]%2==0:
        pares = pares[1]
    if t[2]%2==0:
        pares = pares[2]
    if t[3]%2==0:
        pares = pares[3]
    return pares