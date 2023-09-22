def posLetra(frase, letra, n):
    '''Retorna a posição da letra dada até a ocorrência pedida(n);
    str, str, int -> int'''
    
    i = 0
    n_rep = 0
    
    if letra not in frase:
        return -1
        
    while n != n_rep :
        
        if i == len(frase):
            n_rep == n
            
    	if letra in frase[i]:
                
        	n_rep = n_rep + 1     
    
        i = i + 1
        
    if letra not in frase or n_rep < n:
    	return -1 
    
    return i-1