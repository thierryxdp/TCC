def posLetra (frase, letra, numero):
    i=0
    posicao=0
    while i<len(frase):
        if letra[i] in frase :
            posicao = posicao + numero
       		 i = i+1
        	return posicao
        else:
            return -1