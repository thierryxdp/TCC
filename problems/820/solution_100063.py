def posLetra(string,letra,n):  
    
    i = 0
    ocorrencia = str.count(string,letra)
    
    while i < len(string):
        if letra in string and n <= ocorrencia:    
        	posicao = str.index(string,letra,n)
    	i = i + 1
    
    return posicao