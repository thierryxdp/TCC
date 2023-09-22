def posLetra(letras,l,n):
	'''retorna em que posição da string aquela ocorrência
    da letra está; 
    str,str,int -> int'''
    
    i=0
    
    while n < len(letras):
        if l in letras:
            return i
        
        else:
            return -1
        
    i= i+1
    return i