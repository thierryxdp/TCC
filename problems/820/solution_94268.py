def posLetra (frase, letra, numero):
    i=0
    posicao=0
    while i<len(letra):
        if letra[numero] in frase :
            posicao = posicao - 1
        	return posicao
        else:
            return -1