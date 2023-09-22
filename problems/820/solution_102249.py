def posLetra(texto,letra,ocorrencia):
    tentativa=1
    posicao=str.find(texto, letra)
    
    while tentativa<=ocorrencia:
        if  tentativa<ocorrencia:
        	tentativa+=1
        elif tentativa==ocorrencia:
        	posicao=str.find(texto, letra)
        else:
            posicao = -1
    return posicao