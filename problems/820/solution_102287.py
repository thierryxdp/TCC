def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    posicaoA=0
    while teste_ocorrencia<ocorrencia:
        if str.find(texto, letra,posicaoA) == -1:
        	posicaoA = -1
            return posicao
        elif str.find(texto, letra,posicaoA) != -1:
            posicaoA=str.find(texto, letra,posicaoA)
        	teste_ocorrencia+=1
        elif teste_ocorrencia==ocorrencia:
        	posicaoA= str.find(texto, letra,posicaoA)
            return posicaoA