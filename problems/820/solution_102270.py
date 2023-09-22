def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    while False:
        if str.find(texto, letra, teste_ocorrencia) == -1:
        	posicao = -1
        if str.find(texto, letra,teste_ocorrencia) != -1:
        	teste_ocorrencia+=1
        if teste_ocorrencia==ocorrencia:
        	posicao=str.find(texto, letra,teste_ocorrencia)
    return posicao