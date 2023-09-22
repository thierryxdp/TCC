def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    while teste_ocorrencia<=ocorrencia:
        teste_ocorrencia+=1
        if tentativa==ocorrencia:
        	posicao=str.find(texto, letra,teste_ocorrencia)
        else:
            posicao=-1
    	return posicao