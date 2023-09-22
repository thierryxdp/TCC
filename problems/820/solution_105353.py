def posLetra(string,letra,numero):
    """Calcula e retorna"""
    i=0
    posicao=-1
    acumulador=[]
    if str.count(string,letra)>=numero or letra not in string:
        return posicao
    else:
    	while len(acumulador)<=numero:
        	if string[i] == letra:
            	posicao = i
           		acumulador=acumulador + [string[i]]
        	i=i+1
    	return posicao