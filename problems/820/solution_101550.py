def posLetra(palavra,l,n):
	'''retorna em que posição da string aquela ocorrência
    da letra está; 
    str,str,int -> int'''
    
    i=0
    
    while n < len(palavra):
        
        if palavra[i] == l:
           	x = palavra.index(l,n,n)
            
                
    	i= i+n
    
    return x