def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    posicao=0
    while teste_ocorrencia<=ocorrencia:
        if str.find(texto, letra, posicao) == -1:
        	posicao = -1
            return posicao
        if teste_ocorrencia!=ocorrencia:
            posicao=str.find(texto, letra, posicao)
        	teste_ocorrencia+=1
        if teste_ocorrencia==ocorrencia:
        	posicao= str.find(texto, letra, (posicao))
        	return posicao
    else:
         return -1