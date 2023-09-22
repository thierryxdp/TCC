def posLetra(texto,letra,ocorrencia):
    tentativa=1
    teste_ocorrencia=0
    
    while tentativa<=ocorrencia:
        posicao=str.find(texto, letra, teste_ocorrencia)
        if  str.find(texto,letra,teste_ocorrencia):
            teste_ocorencia+=1
        elif tentativa==ocorrencia:
        	posicao=str.find(texto, letra,teste_ocorrencia)
        else:
            posicao=-1
    	return posicao