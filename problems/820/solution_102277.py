def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    while:
        if str.find(texto, letra, teste_ocorrencia) == -1:
        	posicao = -1
        elif teste_ocorrencia==ocorrencia:
        	posicao = str.find(texto, letra,teste_ocorrencia)
        elif str.find(texto, letra,teste_ocorrencia) != -1:
        	teste_ocorrencia+=1
            
    return posicao