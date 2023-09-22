def posLetra(texto,letra,ocorrencia):
    tentativa=1
    
    while tentativa<=ocorrencia:
        posicao=str.find(texto, letra)
        if  tentativa<ocorrencia:
        	tentativa+=1
        elif tentativa==ocorrencia:
        	posicao=str.find(texto, letra)
            return posicao
        else:
            posicao=-1
    	return posicao