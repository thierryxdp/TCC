def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    if teste_ocorrencia<=ocorrencia:
    	while teste_ocorrencia<=ocorrencia:
        	if str.find(texto, letra,teste_ocorrencia):
        		teste_ocorrencia+=1
        	elif teste_ocorrencia==ocorrencia:
        		posicao=str.find(texto, letra,teste_ocorrencia
    else:
         posicao=-1
    return posicao