def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    posicao=0
	aparece=str.count(texto,letra)
    if aparece<ocorrencia or aparece==0:
    	return -1
    while teste_ocorrencia<ocorrencia:
        if teste_ocorrencia!=ocorrencia:
            posicao=str.find(texto, letra, posicao)
        	teste_ocorrencia+=1
            posicao +=1
    return posicao - 1