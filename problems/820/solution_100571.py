def posLetra(letras,l,n)
	'''retorna em que posição da string aquela ocorrência
    da letra está; 
    str,str,int -> int'''
    
    i=0
    
    while n < len(letras):
        if l in letras[i]:
            return i
        
        i= i+1