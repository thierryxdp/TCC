def posLetra(string,letra,n):  
    
    i = 0
    while i < len(string):
        if letra in string:    
        	posicao = str.find(string[:n],letra,n)
        else:
            posicao = (-1)
    	i = i + 1
    
    return posicao