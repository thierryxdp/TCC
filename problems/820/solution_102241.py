def posLetra(texto,letra,ocorrencia):
    tentativa=1
    while tentativa<ocorrencia:
    	posicao=str.find(texto, letra)
        tentativa+=1
    if tentativa==ocorrencia:
        return posicao
    else:
        return -1