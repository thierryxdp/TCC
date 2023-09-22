def posLetra (frase,letra,ocorrencia):
    ''' função que retorna a posição da letra dada a frase, a letra e o valor de ocorrência
    str,str,int ->int'''
    
    i=0
    contador=-1
    
    while i<len (frase):
		if 0 == ocorrencia:
            return -1
        if frase [i] == letra:
            contador = contador +1
        if contador == ocorrencia:
            return contador
    	i=i+1