def posLetra (s,letra,num):
	posicao = s.find(letra)
	num=0
    while posicao<num and posicao>num :
	        posicao = s.find(letra, posicao + 1)
    num=num+ 1
	return posicao