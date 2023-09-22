def filtra_pares(t:tuple)->tuple:
    
    """ Função que dado uma tupla com 4 números inteiros, retorna somento os valores pares
    
    	Parameters:
        
        t: tupla com 4 números inteiros
        
        returns:
        
        Seqêuncia de if's verificando se cada elemento da tupla é par e criando uma nova tupla com esses elementos 
        
     """
    
    par = ()
    
    if t[0]%2 == 0:
        
        par = par + (t[0],)
        
    if t[1]%2 == 0:
        
        par = par + (t[1],)
        
    if t[2]%2 == 0:
        
        par = par + (t[2],)
        
    if t[3]%2 == 0:
        
        par = par + (t[3],)
        
    return par