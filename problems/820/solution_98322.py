def posLetra(string, letra, ocorrencia):
    '''Função que retorna a posição da letra inserida depois de x ocorrencias da mesma.
    str,str,int --> int'''
    
    i = 0
    l = 0
    
    while(l < ocorrencia and i < len(string)):
        if letra in string[i]:
            l += 1

        i += 1

    	if l == ocorrencia:
        	return i-1
    
    	else:
        	return -1