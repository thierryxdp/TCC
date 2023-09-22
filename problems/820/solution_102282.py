def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    while teste_ocorrencia<len(texto):
        if str.find(texto, letra, teste_ocorrencia) == -1:
        	posicao = -1
            return posicao
        elif teste_ocorrencia<ocorrencia and != -1:
        	teste_ocorrencia+=1
        elif teste_ocorrencia==ocorrencia:
        	posicao = str.find(texto, letra,teste_ocorrencia)
            return posicao