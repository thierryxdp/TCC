def filtra_pares (a,b,c,d):
    
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro e retorne uma nova tupla contendo apenas os elementos pares da tupla original.
    	Exemplo:
        
        Parâmetros: 
        a = 34
        b = 21
        c = 7
        d = 60
        
        return: 34, 60
    	"""
    
    if [a]%2==0:
        return a
    
    if [b]%2==0:
        return b  
    
    if [c]%2==0:
        return c
  
    if [d]%2==0:
        return d
    
    else:
    return ''