def posLetra (s,letra,num):
	posicao = s.find(letra)
    while posicao >= 0 and num > 1 :
	        posicao = s.find(letra, posicao + 1)
    num=1
	return posicao