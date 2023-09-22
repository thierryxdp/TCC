def posLetra (s,letra,num):
	posicao = s.index(letra)
    while posicao >= 0 and num > 1 :
	        posicao = s.index(letra, posicao + 1)
    		num-=1
	return posicao