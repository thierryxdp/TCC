def posLetra(texto,letra,ocorrencia):
    tentativa=1
    while tentativa<ocorrencia:
    	posicao=str.find(texto, letra)
        tentativa+=1
    return posicao