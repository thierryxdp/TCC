def posLetra (s,letra,num):
	posicao = s.find(letra)
	num=0
    while posicao>= 0 and num > 1 :
	        posicao = s.find(letra, posicao + 1)
    num=num+ 1
	return posicao