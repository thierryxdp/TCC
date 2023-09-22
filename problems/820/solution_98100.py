def posLetra(frase,letra,ocorrencia):
    i = 0
    j = 0
    while(i < len(frase)):
        if letra in frase[i]:
            j += 1
            
        if j == ocorrencia:
            return i
     	
        i += 1
        
	return -1