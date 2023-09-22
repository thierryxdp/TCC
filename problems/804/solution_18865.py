def filtra_pares(elementos):
    """ Função que recebe quatro números, 
    	filtra os que são pares e 
        retorna uma nova tupla com a mesma ordem.  
    """
    n1,n2,n3,n4 = elementos
    par = tuple()
    
    if n1 % 2 == 0:
        par += (n1, )
       
    if n2 % 2 == 0:
        par += (n2, )
        
    if n3 % 2 == 0:
        par += (n3, )
    
    if n4 % 2 == 0:
        par += (n4, )
        
    return par