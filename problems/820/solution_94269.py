def posLetra (frase, letra, numero):
    i=numero
    posicao=0
    while i<len(letra):
        if letra[i] in frase :
            posicao = posicao - 1
        	return posicao
        else:
            return -1