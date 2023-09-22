def posLetra(string,letra,numero):
    posicao= str.find(string,letra)
    if str.count(string,letra)>=numero:
    	while numero>1:
            posicao= str.find(string,letra,posicao+1)
            numero= numero - 1
    	return posicao
    else:
        return -1