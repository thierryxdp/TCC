def posLetra(string,letra,n):  
    
    i = 0
    ocorrencia = str.count(string,letra)
    
    while i < len(string):
        if letra in string and n <= ocorrencia:    
        	posicao = str.index(string,letra,ocorrencia)
        else:
            posicao = (-1)
    	i = i + 1
    
    return posicao